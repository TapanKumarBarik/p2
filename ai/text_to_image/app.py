import hashlib
import io
import json
import random
import re
import subprocess
import time
from datetime import datetime
from pathlib import Path

import ollama
import streamlit as st
from PIL import Image, ImageOps, UnidentifiedImageError

HERE = Path(__file__).resolve().parent  # absolute, because sd-cli runs from inside sd/

# Chat model: the FLUX.2 Klein text encoder imported into Ollama (see Modelfile). Text only.
CHAT_MODEL = "flux2-klein"

# Image generation: the three parts of FLUX.2 Klein, run by stable-diffusion.cpp (see README.md)
SD_CLI = next(
    (p for p in (HERE / "sd" / "sd-cli.exe", HERE / "sd-vulkan" / "sd-cli.exe") if p.exists()),
    HERE / "sd" / "sd-cli.exe",
)
DIFFUSION_MODEL = HERE / "models" / "flux-2-klein-4b-Q4_0.gguf"
VAE = HERE / "models" / "flux2-vae.safetensors"
TEXT_ENCODER = HERE / "models" / "flux2-klein-4b-uncensored-q4_k_m.gguf"
OUTPUTS = HERE / "outputs"
REFS = OUTPUTS / "refs"  # uploaded reference images, shrunk and saved for sd-cli
MAX_REFS = 4  # each reference adds work, so more than a few gets slow

SIZES = {
    "Square · 512": (512, 512),
    "Square · 768": (768, 768),
    "Square · 1024": (1024, 1024),
    "Portrait · 768×1024": (768, 1024),
    "Landscape · 1024×768": (1024, 768),
    "Wide · 1280×720": (1280, 720),
}

PROMPT_WRITER = (
    "You turn short ideas into detailed prompts for an image generator. "
    "Reply with a single paragraph describing the subject, setting, lighting, "
    "mood, colors, camera angle and art style. No preamble, no explanations."
)
CHAT_SYSTEM_PROMPTS = {
    "Prompt writer": PROMPT_WRITER,
    "Chat": "You are a helpful assistant.",
}

# Clickable ideas on the Create tab: category -> {short label: full prompt}
SUGGESTIONS = {
    "Photo": {
        "Rainy café cat": "a ginger cat reading a book at a wooden table in a cozy cafe, rain on the window, warm amber light, shallow depth of field, photorealistic",
        "Mountain sunrise": "misty mountain valley at sunrise, golden light breaking through the clouds, pine forest, mirror-like lake reflection, landscape photography, ultra detailed",
        "Old fisherman": "portrait of an elderly fisherman with a weathered face and a knitted cap, soft window light, 85mm lens, film grain, black and white photography",
        "Tokyo at night": "neon-lit Tokyo alley at night after rain, glowing signs reflecting in puddles, people with umbrellas, cinematic 35mm photo",
    },
    "Art": {
        "Watercolor fox": "a red fox curled up asleep in autumn leaves, loose watercolor painting, soft bleeding colors, white paper texture",
        "Oil painting harbor": "a small fishing harbor at dusk, impressionist oil painting, thick brush strokes, warm orange and deep blue palette",
        "Pixel art castle": "a floating castle on a cloud island with waterfalls pouring off the edges, 16-bit pixel art, vibrant colors",
        "Low-poly island": "a tiny tropical island with a palm tree and a lighthouse, low-poly 3D render, isometric view, bright pastel colors",
    },
    "Fantasy": {
        "Dragon library": "an ancient library inside a giant tree, a small dragon sleeping on a stack of books, floating candles, magical glow, fantasy illustration",
        "Garden on Mars": "an astronaut tending a glowing garden inside a glass dome on Mars, red desert outside, soft rim light, cinematic sci-fi",
        "Cyberpunk samurai": "a cyberpunk samurai standing on a rooftop in the rain, glowing katana, holographic billboards, dramatic lighting, concept art",
        "Underwater city": "a bioluminescent underwater city with coral towers and jellyfish lanterns, deep blue water, light rays from above, digital painting",
    },
    "Product": {
        "Ramen bowl": "a steaming bowl of ramen with a soft-boiled egg, chashu and green onions on a dark wooden table, moody food photography, top-down angle",
        "Sneaker ad": "a white sneaker floating above a pastel pink background, soft shadows, clean studio product photography, high detail",
        "Coffee splash": "a coffee cup with a dramatic splash of coffee frozen in mid-air, coffee beans flying, dark background, high-speed photography",
        "Perfume bottle": "a luxury glass perfume bottle on black marble surrounded by rose petals, golden rim light, elegant commercial photography",
    },
    "Fun": {
        "Corgi chef": "a corgi wearing a chef's hat cooking pancakes in a tiny kitchen, 3D animated movie style, warm lighting, adorable",
        "Cat astronaut": "a fluffy cat in an astronaut suit floating in space, Earth in the background, stars, playful and cinematic",
        "Penguin DJ": "a penguin DJ wearing headphones in a neon nightclub, a crowd of dancing penguins, vibrant party lights, cartoon style",
        "Skateboarding sloth": "a smiling sloth riding a skateboard down a sunny beach boardwalk, motion blur, bright summer colors, photorealistic",
    },
}
CATEGORY_ICONS = {
    "Photo": ":material/photo_camera:",
    "Art": ":material/brush:",
    "Fantasy": ":material/auto_awesome:",
    "Product": ":material/shopping_bag:",
    "Fun": ":material/mood:",
}

# Clickable edit ideas, shown once there's a reference image. The model knows references as "image 1", "image 2", ...
EDIT_IDEAS = {
    "Watercolor": "turn image 1 into a soft watercolor painting, keep the same composition",
    "Anime style": "redraw image 1 in a hand-painted anime movie style, keep the same composition",
    "Wizard hat": "put a small purple wizard hat on the main subject of image 1, keep everything else the same",
    "Winter": "make image 1 a snowy winter scene, keep everything else the same",
    "Night + neon": "change image 1 to night time with glowing neon lights, keep everything else the same",
    "3D figurine": "turn the main subject of image 1 into a cute 3D collectible figurine standing on a desk",
    "Studio background": "replace the background of image 1 with a clean white studio background, keep the subject exactly the same",
    "Combine 1 + 2": "the main subject of image 1 placed into the scene of image 2, matching the lighting and style of image 2",
}

# Clickable starters on the Prompt assistant tab (shown while the chat is empty)
CHAT_STARTERS = {
    "Prompt writer": ["a cozy cabin in a snowstorm", "a robot learning to paint", "a city built on clouds", "a tiger made of flowers"],
    "Chat": ["Give me 5 creative image ideas", "Write a haiku about rain", "Suggest names for a pet robot"],
}

# sd-cli prints sampling progress like "|=====>     | 2/4 - 1.20it/s"
STEP_RE = re.compile(r"\|\s*(\d+)/(\d+) - [\d.]+(?:s/it|it/s)")


# ---------- callbacks (run before the page redraws, so they can change widget values) ----------

def use_prompt(text):
    st.session_state.img_prompt = text


def surprise():
    category = random.choice(list(SUGGESTIONS.values()))
    use_prompt(random.choice(list(category.values())))


def pick_idea(key, ideas):
    # Pills act like buttons here: fill the prompt, then un-select
    if choice := st.session_state[key]:
        use_prompt(ideas[choice])
    st.session_state[key] = None


def send_to_generator(text):
    use_prompt(text)
    st.session_state.toast = ("Prompt sent to the Create tab.", ":material/check_circle:")


def queue_starter():
    # A clicked starter pill is sent as if it was typed into the chat box
    st.session_state.queued_msg = st.session_state.starter
    st.session_state.starter = None


def clear_chat():
    st.session_state.messages = []


def select_image(path):
    st.session_state.selected = path


def edit_image(path):
    # Start a new round of edits on this image: it becomes image 1
    st.session_state.picked_refs = [path]
    st.session_state.toast = ("Now it's image 1. Describe the change or pick an edit idea.", ":material/edit:")


def add_reference(path):
    if path not in st.session_state.picked_refs:
        st.session_state.picked_refs.append(path)
    st.session_state.toast = (f"Added as image {st.session_state.picked_refs.index(path) + 1}.", ":material/add_photo_alternate:")


def clear_picked_refs():
    st.session_state.picked_refs = []


def delete_image(path):
    png = Path(path)
    if png.parent != OUTPUTS or png.suffix != ".png":  # only ever delete generated images
        return
    png.unlink(missing_ok=True)
    png.with_suffix(".json").unlink(missing_ok=True)
    if st.session_state.get("selected") == path:
        del st.session_state.selected
    st.session_state.picked_refs = [r for r in st.session_state.picked_refs if r != path]
    st.session_state.toast = ("Image deleted.", ":material/delete:")


# ---------- helpers ----------

def show(content, as_code):
    # Prompts go in a code block so they get a one-click copy button
    if as_code:
        st.code(content, language=None, wrap_lines=True)
    else:
        st.markdown(content)


def gpu_backend():
    folder = SD_CLI.parent
    if (folder / "ggml-cuda.dll").exists():
        return "CUDA"
    return "Vulkan" if (folder / "ggml-vulkan.dll").exists() else "CPU"


@st.cache_data(ttl=10, show_spinner=False)
def assistant_online():
    try:
        return any(m.model.split(":")[0] == CHAT_MODEL for m in ollama.list().models)
    except Exception:
        return False


def free_gpu():
    """Unload the Ollama chat model so sd-cli gets all 6 GB of VRAM."""
    try:
        if any(m.model.startswith(CHAT_MODEL) for m in ollama.ps().models):
            ollama.generate(model=CHAT_MODEL, keep_alive=0)
    except Exception:
        pass  # Ollama isn't running, so there's nothing to free


def enhance_prompt(idea):
    response = ollama.chat(
        model=CHAT_MODEL,
        messages=[{"role": "system", "content": PROMPT_WRITER}, {"role": "user", "content": idea}],
        think=False,
        keep_alive=0,  # unload right away so the GPU is free for image generation
        options={"temperature": 0.7},
    )
    return response.message.content.strip()


def generate_image(prompt, width, height, steps, seed, refs, out_path, on_progress):
    """Run sd-cli and report progress. Returns (success, log lines)."""
    cmd = [
        str(SD_CLI),
        "--diffusion-model", str(DIFFUSION_MODEL),
        "--vae", str(VAE),
        "--llm", str(TEXT_ENCODER),
        "-p", prompt,
        "--cfg-scale", "1.0",
        "--steps", str(steps),
        "-W", str(width),
        "-H", str(height),
        "-s", str(seed),
        "--offload-to-cpu",
        "--diffusion-fa",
        "-o", str(out_path),
    ]
    for ref in refs:  # FLUX.2 edits/combines these; the prompt calls them image 1, image 2, ...
        cmd += ["-r", ref]
    proc = subprocess.Popen(
        cmd,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        bufsize=0,
        cwd=SD_CLI.parent,
        creationflags=getattr(subprocess, "CREATE_NO_WINDOW", 0),
    )
    log, pending = [], ""
    try:
        while chunk := proc.stdout.read(4096):
            pending += chunk.decode("utf-8", "replace")
            # Progress bars redraw with \r, normal log lines end with \n
            *lines, pending = re.split(r"[\r\n]", pending)
            for line in lines:
                line = line.replace("\x1b[K", "").strip()
                if not line:
                    continue
                log.append(line)
                if "loading diffusion model" in line:
                    on_progress(0.05, "Loading models…")
                elif "get_learned_condition completed" in line:
                    on_progress(0.2, "Reading the prompt…")
                elif match := STEP_RE.search(line):
                    done, total = int(match[1]), int(match[2])
                    on_progress(0.2 + 0.65 * done / total, f"Generating · step {done} of {total}")
                elif "decoding" in line and "latents" in line:
                    on_progress(0.9, "Finishing…")
        proc.wait()
    finally:
        if proc.poll() is None:  # the user left mid-run, so don't leave sd-cli running
            proc.kill()
    return proc.returncode == 0 and out_path.exists(), log


def load_gallery(limit=12):
    items = []
    for png in sorted(OUTPUTS.glob("*.png"), key=lambda p: p.stat().st_mtime, reverse=True)[:limit]:
        meta_file = png.with_suffix(".json")
        meta = json.loads(meta_file.read_text(encoding="utf-8")) if meta_file.exists() else {}
        items.append((png, meta))
    return items


@st.cache_data(show_spinner=False, max_entries=64)
def thumbnail(path, mtime):
    # Square crops keep the gallery grid even; mtime is part of the cache key so a changed file gets a new thumbnail
    img = ImageOps.fit(Image.open(path).convert("RGB"), (320, 320))
    buf = io.BytesIO()
    img.save(buf, "JPEG", quality=88)
    return buf.getvalue()


def save_reference(upload):
    """Shrink an uploaded image (phone photos can be 12+ MP) and save it where sd-cli can read it."""
    data = upload.getvalue()
    path = REFS / f"{hashlib.sha1(data).hexdigest()[:12]}.png"
    if not path.exists():
        img = ImageOps.exif_transpose(Image.open(io.BytesIO(data))).convert("RGB")  # respect phone rotation
        img.thumbnail((1024, 1024))
        REFS.mkdir(parents=True, exist_ok=True)
        img.save(path)
    return str(path)


def fit_to_reference(path, area):
    """Width and height with the reference's shape, about `area` pixels, sides a multiple of 16."""
    w, h = Image.open(path).size
    scale = (area / (w * h)) ** 0.5
    return round(w * scale / 16) * 16, round(h * scale / 16) * 16


def meta_badges(meta):
    parts = [f"{meta['width']}×{meta['height']}", f"seed {meta['seed']}", f"{meta['steps']} steps", f"{meta['seconds']} s"]
    if n := meta.get("references"):
        parts.append(f"{n} reference{'s' if n > 1 else ''}")
    return " ".join(f":gray-badge[{p}]" for p in parts)


# ---------- Create tab ----------

def render_references():
    """Reference image panel. Returns (reference paths, keep image 1's shape)."""
    picked = st.session_state.picked_refs
    refs, match_shape = list(picked), False
    with st.expander("Reference images", icon=":material/add_photo_alternate:", expanded=bool(picked)):
        st.caption("Upload a photo to edit it, or two or more to combine them. In the prompt they're called image 1, image 2, …")
        uploads = st.file_uploader(
            "Reference images", type=["png", "jpg", "jpeg", "webp"], accept_multiple_files=True, label_visibility="collapsed",
        )
        for upload in uploads or []:
            try:
                refs.append(save_reference(upload))
            except UnidentifiedImageError:
                st.warning(f"Couldn't read {upload.name} as an image, so it was skipped.", icon=":material/warning:")
        refs = list(dict.fromkeys(refs))  # the same image twice is just one reference
        if len(refs) > MAX_REFS:
            st.warning(f"Using the first {MAX_REFS} images. Each extra reference makes generation slower.", icon=":material/warning:")
            refs = refs[:MAX_REFS]

        if refs:
            cols = st.columns(MAX_REFS)
            for i, ref in enumerate(refs):
                cols[i].image(ref, caption=f"image {i + 1}", width="stretch")
            match_shape = st.toggle("Keep image 1's aspect ratio", value=True, help="The Size setting still controls how detailed the result is.")
            ideas = {k: v for k, v in EDIT_IDEAS.items() if "image 2" not in v or len(refs) > 1}
            st.pills("Edit ideas", list(ideas), key="edit_ideas", on_change=pick_idea, args=("edit_ideas", ideas))
            if picked:
                st.button("Clear images picked from the gallery", icon=":material/close:", type="tertiary", on_click=clear_picked_refs)
    return refs, match_shape


def render_create_tab():
    missing = [p for p in (SD_CLI, DIFFUSION_MODEL, VAE, TEXT_ENCODER) if not p.exists()]
    if missing:
        st.error(
            "Image generation needs these files, which are missing:\n\n"
            + "\n".join(f"- `{p.relative_to(HERE)}`" for p in missing)
            + "\n\nRun `python setup.py` in this folder to download them (safe to run again; it resumes).",
            icon=":material/error:",
        )
        return

    left, right = st.columns([5, 7], gap="large")

    with left:
        with st.container(border=True):
            # "Enhance" can't write into the text box after it's drawn, so it parks the result here for the rerun
            if "pending_prompt" in st.session_state:
                st.session_state.img_prompt = st.session_state.pop("pending_prompt")
            prompt = st.text_area(
                "Prompt", key="img_prompt", height=130, placeholder="Describe the image you want to create…",
            ).strip()
            with st.container(horizontal=True, gap="small"):
                enhance = st.button("Enhance prompt", icon=":material/auto_fix_high:", type="tertiary",
                                    help="The local assistant rewrites your idea into a detailed prompt")
                st.button("Surprise me", icon=":material/casino:", type="tertiary", on_click=surprise)

            st.markdown("**Inspiration**")
            first = next(iter(SUGGESTIONS))
            category = st.segmented_control(
                "Category", list(SUGGESTIONS), default=first, key="category",
                format_func=lambda c: f"{CATEGORY_ICONS[c]} {c}", label_visibility="collapsed",
            ) or first
            ideas = SUGGESTIONS[category]
            key = f"ideas_{category}"
            st.pills("Ideas", list(ideas), key=key, on_change=pick_idea, args=(key, ideas), label_visibility="collapsed")

        refs, match_shape = render_references()

        with st.container(border=True):
            c1, c2 = st.columns([3, 2])
            size_label = c1.selectbox("Size", list(SIZES), help="Bigger is sharper but slower: 512 ≈ 12 s, 1024 ≈ 27 s")
            steps = c2.number_input("Steps", 1, 8, 4, help="FLUX.2 Klein is trained for 4 steps. More rarely helps.")
            c3, c4 = st.columns([3, 2], vertical_alignment="bottom")
            fixed = c4.toggle("Fixed seed", help="Same prompt + same seed = same image")
            seed_value = c3.number_input("Seed", 0, 2**31 - 1, 42, disabled=not fixed)

        generate = st.button("Generate", type="primary", icon=":material/auto_awesome:", width="stretch")

        if (generate or enhance) and not prompt:
            st.warning("Write a prompt or pick an idea first.", icon=":material/edit_note:")
        elif enhance:
            try:
                with st.spinner("Enhancing prompt…"):
                    st.session_state.pending_prompt = enhance_prompt(prompt)
                st.rerun()
            except (ConnectionError, ollama.ResponseError):
                st.warning("The prompt assistant isn't available. Start Ollama, or generate with your prompt as it is.", icon=":material/cloud_off:")

    with right:
        if generate and prompt:
            width, height = SIZES[size_label]
            if refs and match_shape:
                width, height = fit_to_reference(refs[0], width * height)
            seed = int(seed_value) if fixed else random.randint(0, 2**31 - 1)
            OUTPUTS.mkdir(exist_ok=True)
            out = OUTPUTS / f"{datetime.now():%Y%m%d-%H%M%S}_{seed}.png"

            slot = st.empty()
            with slot.container(border=True):
                bar = st.progress(0.0, text="Starting…")
            free_gpu()
            start = time.time()
            ok, log = generate_image(prompt, width, height, steps, seed, refs, out, lambda v, t: bar.progress(v, text=t))
            slot.empty()

            if ok:
                meta = {"prompt": prompt, "seed": seed, "width": width, "height": height,
                        "steps": steps, "seconds": round(time.time() - start, 1), "references": len(refs)}
                out.with_suffix(".json").write_text(json.dumps(meta, indent=2), encoding="utf-8")
                st.session_state.selected = str(out)
            else:
                st.error("Generation failed. Try a smaller size, or the Vulkan build (README → Troubleshooting).", icon=":material/error:")
                with st.expander("sd-cli output (last 30 lines)"):
                    st.code("\n".join(log[-30:]), language=None)

        gallery = load_gallery()
        by_path = {str(p): (p, m) for p, m in gallery}
        current = by_path.get(st.session_state.get("selected")) or (gallery[0] if gallery else None)

        if current:
            png, meta = current
            with st.container(border=True):
                st.image(str(png), width="stretch")
                if meta:
                    st.markdown(meta_badges(meta))
                    st.caption(meta["prompt"])
                with st.container(horizontal=True, gap="small"):
                    st.download_button("Download", png.read_bytes(), file_name=png.name, mime="image/png",
                                       icon=":material/download:", on_click="ignore")
                    st.button("Edit this image", icon=":material/edit:", key="edit_current",
                              on_click=edit_image, args=(str(png),), help="Use it as image 1 and keep changing it")
                    if meta.get("prompt"):
                        st.button("Reuse prompt", icon=":material/replay:", key="reuse_current",
                                  on_click=use_prompt, args=(meta["prompt"],))
                    with st.popover("Delete", icon=":material/delete:", type="tertiary", key="delete_current"):
                        st.markdown("Delete this image? This can't be undone.")
                        st.button("Delete image", type="primary", key="confirm_delete_current",
                                  on_click=delete_image, args=(str(png),))
        else:
            with st.container(border=True, height=520, horizontal_alignment="center", vertical_alignment="center"):
                st.markdown("## :gray[:material/image:]", text_alignment="center", anchors=False)
                st.markdown("**Your images will appear here**", text_alignment="center")
                st.markdown(":gray[Write a prompt or pick an idea, then press Generate.]", text_alignment="center")

    if gallery:
        st.markdown("##### Recent")
        cols = st.columns(6)
        for i, (png, meta) in enumerate(gallery):
            with cols[i % 6], st.container(border=True, gap="small"):
                st.image(thumbnail(str(png), png.stat().st_mtime), width="stretch")
                with st.container(horizontal=True, gap="small", horizontal_alignment="center"):
                    st.button("", icon=":material/open_in_full:", key=f"view_{png.stem}", type="tertiary",
                              help="Show this image", on_click=select_image, args=(str(png),))
                    if meta.get("prompt"):
                        st.button("", icon=":material/replay:", key=f"reuse_{png.stem}", type="tertiary",
                                  help=f"Reuse prompt: {meta['prompt']}", on_click=use_prompt, args=(meta["prompt"],))
                    st.button("", icon=":material/add_photo_alternate:", key=f"ref_{png.stem}", type="tertiary",
                              help="Add as a reference image", on_click=add_reference, args=(str(png),))
                    with st.popover("", icon=":material/delete:", type="tertiary", key=f"del_{png.stem}", help="Delete"):
                        st.markdown("Delete this image?")
                        st.button("Delete", type="primary", key=f"confirm_del_{png.stem}",
                                  on_click=delete_image, args=(str(png),))


# ---------- Prompt assistant tab ----------

def render_assistant_tab():
    _, mid, _ = st.columns([1, 4, 1])
    with mid:
        with st.container(horizontal=True, vertical_alignment="center", gap="small"):
            mode = st.segmented_control("Mode", list(CHAT_SYSTEM_PROMPTS), default="Prompt writer", key="chat_mode",
                                        required=True, label_visibility="collapsed")
            with st.popover("Settings", icon=":material/tune:", type="tertiary"):
                think = st.toggle("Show thinking", key="think", help="Qwen3 reasons before answering. Slower, but you can see why.")
                temperature = st.slider("Creativity", 0.0, 1.5, 0.6, 0.1, key="temperature",
                                        help="Temperature: higher is more creative, lower is more predictable.")
            st.button("Clear", icon=":material/delete_sweep:", type="tertiary", on_click=clear_chat)

        if not st.session_state.messages:
            with st.container(border=True, horizontal_alignment="center", gap="small"):
                st.markdown("#### What do you want to create?", text_alignment="center")
                intro = ("Describe a rough idea and get a detailed prompt to send to Create." if mode == "Prompt writer"
                         else "A general assistant. It's a small local model, so double-check facts.")
                st.markdown(f":gray[{intro}]", text_alignment="center")
                st.pills("Try one", CHAT_STARTERS[mode], key="starter", on_change=queue_starter, label_visibility="collapsed")

        for i, msg in enumerate(st.session_state.messages):
            avatar = ":material/person:" if msg["role"] == "user" else ":material/auto_awesome:"
            with st.chat_message(msg["role"], avatar=avatar):
                show(msg["content"], msg.get("as_code", False))
                if msg.get("as_code"):
                    st.button("Send to Create", icon=":material/arrow_outward:", key=f"use_{i}",
                              on_click=send_to_generator, args=(msg["content"],))

        placeholder = "Describe an image idea…" if mode == "Prompt writer" else "Ask anything…"
        user_input = st.chat_input(placeholder) or st.session_state.pop("queued_msg", None)
        if not user_input:
            return

        st.session_state.messages.append({"role": "user", "content": user_input})
        with st.chat_message("user", avatar=":material/person:"):
            st.markdown(user_input)

        history = [{"role": "system", "content": CHAT_SYSTEM_PROMPTS[mode]}] + [
            {"role": m["role"], "content": m["content"]} for m in st.session_state.messages
        ]

        with st.chat_message("assistant", avatar=":material/auto_awesome:"):
            thinking_area = st.expander("Thinking", expanded=True).empty() if think else None
            answer_area = st.empty()
            thinking, answer = "", ""

            try:
                stream = ollama.chat(
                    model=CHAT_MODEL,
                    messages=history,
                    think=think,
                    stream=True,
                    options={"temperature": temperature},
                )
                for chunk in stream:
                    if chunk.message.thinking:
                        thinking += chunk.message.thinking
                        thinking_area.markdown(thinking)
                    if chunk.message.content:
                        answer += chunk.message.content
                        answer_area.markdown(answer + "▌")
            except ConnectionError:
                st.session_state.messages.pop()  # drop the unanswered question so a retry starts clean
                st.error("Can't reach Ollama. Start it (open the Ollama app or run `ollama serve`) and try again.", icon=":material/cloud_off:")
                return
            except ollama.ResponseError as e:
                st.session_state.messages.pop()
                st.error(f"Ollama error: {e.error}. Did you run `ollama create {CHAT_MODEL} -f ./Modelfile`?", icon=":material/error:")
                return

        st.session_state.messages.append(
            {"role": "assistant", "content": answer.strip(), "as_code": mode == "Prompt writer"}
        )
        st.rerun()  # redraw so the new answer gets its "Send to Create" button


# ---------- page ----------

st.set_page_config(page_title="Flux2 Klein Studio", page_icon=":material/palette:", layout="wide")
st.html("<style>[data-testid='stMainBlockContainer'] { padding-top: 2.5rem; }</style>")

st.session_state.setdefault("messages", [])
st.session_state.setdefault("img_prompt", "")
st.session_state.setdefault("picked_refs", [])  # gallery images chosen as references (uploads come from the uploader)
if toast := st.session_state.pop("toast", None):
    st.toast(toast[0], icon=toast[1])

models_ready = all(p.exists() for p in (SD_CLI, DIFFUSION_MODEL, VAE, TEXT_ENCODER))
title, status = st.columns([3, 2], vertical_alignment="center")
with title:
    st.markdown("### :material/palette: Flux2 Klein Studio")
    st.caption("Text-to-image and image editing with FLUX.2 Klein 4B, running entirely on this computer.")
with status:
    st.markdown(
        " ".join([
            f":blue-badge[:material/memory: GPU · {gpu_backend()}]",
            ":green-badge[:material/check_circle: Models ready]" if models_ready else ":red-badge[:material/error: Models missing]",
            ":green-badge[:material/forum: Assistant online]" if assistant_online() else ":gray-badge[:material/forum: Assistant offline]",
            ":gray-badge[:material/lock: Local only]",
        ]),
        text_alignment="right",
    )

create_tab, assistant_tab = st.tabs([":material/brush: Create", ":material/forum: Prompt assistant"])
with create_tab:
    render_create_tab()
with assistant_tab:
    render_assistant_tab()

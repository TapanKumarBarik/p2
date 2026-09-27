from __future__ import annotations

import argparse
import ctypes
import time

ES_CONTINUOUS = 0x80000000
ES_SYSTEM_REQUIRED = 0x00000001
ES_DISPLAY_REQUIRED = 0x00000002


def stay_awake(keep_display_on: bool = True) -> None:
    flags = ES_CONTINUOUS | ES_SYSTEM_REQUIRED
    if keep_display_on:
        flags |= ES_DISPLAY_REQUIRED
    ctypes.windll.kernel32.SetThreadExecutionState(flags)


def release() -> None:
    ctypes.windll.kernel32.SetThreadExecutionState(ES_CONTINUOUS)


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Prevent Windows from sleeping or locking the display while this runs."
    )
    parser.add_argument(
        "--minutes", type=float, default=0,
        help="Stop automatically after N minutes (default: run until Ctrl+C).",
    )
    parser.add_argument(
        "--allow-display-off", action="store_true",
        help="Keep the system from sleeping but let the screen still turn off.",
    )
    args = parser.parse_args()

    deadline = time.monotonic() + args.minutes * 60 if args.minutes > 0 else None
    print("Keeping this machine awake. Press Ctrl+C to stop.")

    try:
        while True:
            stay_awake(keep_display_on=not args.allow_display_off)
            if deadline and time.monotonic() >= deadline:
                break
            time.sleep(30)
    except KeyboardInterrupt:
        pass
    finally:
        release()
        print("Stopped. Normal sleep/lock behavior restored.")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())

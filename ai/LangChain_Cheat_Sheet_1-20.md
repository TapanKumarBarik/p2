# LangChain Cheat Sheet + 100 Interview Questions

> Complete notes extracted from the 20-slide LangChain carousel.
>
> **Structure:** Slide 1 is the cover. Slides 2–20 correspond to the handwritten pages 1–19.

---

# 1. Cover

## Complete LangChain Cheat Sheet + 100 Interview Questions

Everything you need to:

- Understand LangChain
- Learn core concepts and APIs
- Work with RAG + Agents
- Use tools and integrations
- Apply production best practices
- Build real-world LangChain applications
- Prepare for interviews

Core flow:

```text
Documents
   ↓
Split
   ↓
Embed
   ↓
Vector Store
   ↓
Retriever
   ↓
LLM + Agent
   ↓
Answer / Action
```

---

## Contents

1. Cover
2. LangChain Introduction + Why LangChain?
3. Installation + Project Setup
4. Models + LLMs + Chat Models
5. Prompts + Prompt Templates
6. Messages + Message History
7. Chains + LCEL
8. Output Parsers + Structured Output
9. Embeddings + Vector Stores
10. Document Loaders + Text Splitters
11. Retrievers + RAG
12. Tools + Tool Calling
13. Agents + Agent Loops
14. Memory + Conversation History
15. Callbacks + Streaming
16. LangGraph Fundamentals
17. Multi Agent Systems + Workflows
18. LangSmith + Tracing + Evaluation
19. Security + Guardrails + Production
20. End to End LangChain RAG + Agent Project

---

# 2. LangChain Introduction + Why LangChain?

## 1. What is LangChain?

- LangChain is an open-source framework for building applications with Large Language Models (LLMs).
- It provides tools, abstractions and reusable components to connect LLMs with real-world data, tools and workflows.
- It helps developers move from experiments to production faster.
- It supports multiple LLM providers such as OpenAI, Anthropic, Google and Meta.
- It integrates with many tools and data sources.

> **LangChain makes it easier to build LLM-powered applications.**

## 2. Why LangChain?

- Simplifies LLM application development.
- Provides prebuilt components such as chains, agents, tools and memory.
- Makes integration with external data such as PDFs, databases and APIs easier.
- Works with multiple LLM providers.
- Helps build RAG applications.
- Supports complex workflows and agent systems.
- Actively maintained with a large community.
- Used by startups and enterprises in production.

> Focus on building your idea, not reinventing the plumbing.

## 3. Key Features of LangChain

- Modular and flexible architecture.
- Chains for building LLM workflows.
- Agents to use tools and perform actions.
- Memory to maintain conversation context.
- Integrations with vector stores, databases, APIs and more.
- LangGraph for building stateful multi-agent workflows.
- LangSmith for debugging, tracing and evaluation.
- Production-ready documentation and integrations.

## 4. LangChain Ecosystem

| Component | Purpose |
|---|---|
| LangChain | Core framework for building LLM applications |
| LangGraph | Stateful and controllable agent workflows |
| LangSmith | Tracing, debugging, evaluation and monitoring |
| LangServe | Deploy LangChain applications as APIs |
| LangChain Hub | Prebuilt prompts, chains and agents |
| Integrations | LLM providers, vector DBs, APIs, tools and more |

## 5. High-Level Architecture

```text
                    ┌───────────────┐
                    │     LLMs      │
                    │ OpenAI, etc.  │
                    └───────┬───────┘
                            │
User                        │
(Query / Input)             ▼
   │                 ┌───────────────┐
   └───────────────► │   LangChain   │
                     │ Chains/Agents │
                     │ Tools/Memory  │
                     └───────┬───────┘
                             ↕
                     ┌───────────────┐
                     │ External Data │
                     │ DB/PDF/API/   │
                     │ Vector Store  │
                     └───────┬───────┘
                             │
                             ▼
                       Response
                    (Answer / Action)
```

## 6. Real-World Use Cases

- Chat with your own documents such as PDFs, notes and reports.
- Build AI-powered customer-support bots.
- Connect LLMs with databases to answer business questions.
- Automate tasks using agents and tools.
- Build research assistants.
- Create domain-specific copilots for education, healthcare, finance and other domains.

> LangChain is not just a library. It is a toolkit for building real-world LLM applications.

---

# 3. Installation + Project Setup

## 1. Prerequisites

- Basic Python knowledge.
- Familiarity with terminal / command line.
- Python 3.9 or above, with 3.10+ recommended.
- A code editor such as VS Code.
- Optional: Git for version control.

> A good setup saves hours of debugging later.

## 2. Install Python and Check Version

### Windows

```bash
python --version
python3 --version
```

### macOS / Linux

```bash
python3 --version
```

You should see Python 3.9 or higher. If not, download Python from the official Python website.

## 3. Create a Virtual Environment

Using `venv`:

```bash
python -m venv .venv
```

### Windows

```bash
.venv\Scripts\activate
```

### macOS / Linux

```bash
source .venv/bin/activate
```

Your terminal prompt should show something like:

```text
(.venv)
```

## 4. Install LangChain and Dependencies

```bash
pip install langchain
```

Common additional packages:

```bash
pip install langchain-openai
pip install langchain-community
pip install langchain-core
pip install python-dotenv
pip install chromadb
pip install faiss-cpu
```

Install only the packages needed for your project.

## 5. Verify Installation

Check installed packages:

```bash
# Windows
pip list | findstr langchain

# macOS / Linux
pip list | grep langchain
```

Test in Python:

```python
import langchain

print(langchain.__version__)
```

If there is no error, LangChain is installed successfully.

## 6. Project Folder Structure

```text
my-langchain-app/
│
├── .venv/              # virtual environment
├── .env                # environment variables
├── app/                # source code
├── notebooks/          # experiments
├── data/               # data files
├── requirements.txt    # dependencies
└── README.md           # project description
```

## 7. Create a `.env` File

Do not hardcode API keys.

```env
OPENAI_API_KEY=your_openai_key_here
LANGCHAIN_TRACING_V2=true
LANGCHAIN_API_KEY=your_langsmith_key
```

## 8. Test a Simple LangChain Setup

Create `app/test.py`:

```python
from dotenv import load_dotenv
load_dotenv()

from langchain.chat_models import ChatOpenAI
from langchain.schema import HumanMessage

llm = ChatOpenAI(model="gpt-3.5-turbo")

response = llm.invoke(
    [HumanMessage(content="Hello from LangChain!")]
)

print(response.content)
```

Run:

```bash
python app/test.py
```

You should see a response from the model.

> Setup is the first step towards turning ideas into real-world applications.

---

# 4. Models + LLMs + Chat Models

## 1. What are Models in LangChain?

- Models are the core of LangChain.
- They act as an interface between your application and different LLM providers.
- LangChain provides a unified way to work with different models using the same API.
- You can switch between models without changing the entire application logic.

> Same code, different model. That's the power of abstraction.

## 2. Types of Models

| Type | Description |
|---|---|
| LLMs | General-purpose text-completion models |
| Chat Models | Optimized for chat conversations |
| Embedding Models | Convert text into vectors |
| Multimodal Models | Handle text, images, audio and other modalities |
| Local Models | Run models on your own machine |

## 3. Popular LLM Providers

| Provider | Example Models | Typical Use |
|---|---|---|
| OpenAI | GPT-3.5, GPT-4o | General-purpose applications |
| Anthropic | Claude 3 Haiku, Claude 3 Sonnet | Long-context and reasoning |
| Google | Gemini 1.5 Pro, Gemini 1.5 Flash | Multimodal and large context |
| Meta | Llama 3 | Open-source / local use |
| Mistral | Mistral Large, Medium | High-performance open models |
| Cohere | Command-a, Command-r-plus | Enterprise use cases |
| Ollama | Llama, Mistral, etc. | Local execution |

## 4. Using LLM (Text Completion)

```python
from langchain.llms import OpenAI

llm = OpenAI(
    model="gpt-3.5-turbo-instruct",
    temperature=0.7
)

response = llm.invoke("Explain MLOps in simple words.")
print(response)
```

LLMs are used for single-turn text completion rather than chat-style message interactions.

## 5. Using a Chat Model

```python
from langchain.chat_models import ChatOpenAI
from langchain.schema import HumanMessage, SystemMessage

chat = ChatOpenAI(
    model="gpt-3.5-turbo",
    temperature=0.7
)

messages = [
    SystemMessage(content="You are a helpful assistant."),
    HumanMessage(content="Explain LangChain in simple words.")
]

response = chat.invoke(messages)
print(response.content)
```

> Chat models are commonly used in modern applications.

## 6. Passing Parameters

```python
chat = ChatOpenAI(
    model="gpt-4o",
    temperature=0.3,
    max_tokens=500,
    top_p=1.0,
    frequency_penalty=0.0,
    presence_penalty=0.0
)
```

| Parameter | Meaning |
|---|---|
| `model` | Model to use |
| `temperature` | Controls randomness |
| `max_tokens` | Maximum response length |
| `top_p` | Nucleus sampling |
| `frequency_penalty` | Reduces repetitive text |
| `presence_penalty` | Encourages new topics |

## 7. Switching Between Models

The same application can use different providers:

```python
# OpenAI
from langchain_openai import ChatOpenAI
chat = ChatOpenAI(model="gpt-3.5-turbo")
```

```python
# Anthropic
from langchain_anthropic import ChatAnthropic
chat = ChatAnthropic(model="claude-3-sonnet")
```

```python
# Google / Gemini
from langchain_google_genai import ChatGoogleGenerativeAI
chat = ChatGoogleGenerativeAI(model="gemini-1.5-pro")
```

```python
# Ollama
from langchain_community.chat_models import ChatOllama
chat = ChatOllama(model="llama3")
```

## 8. Model with Streaming

```python
chat = ChatOpenAI(
    model="gpt-3.5-turbo",
    streaming=True
)

for chunk in chat.stream(
    [HumanMessage(content="Tell me a story about AI.")]
):
    print(chunk.content, end="", flush=True)
```

> Streaming gives real-time responses token by token.

## 9. Best Practices

- Choose the right model for the use case.
- Set an appropriate temperature.
- Use system messages for better control.
- Handle errors and retries.
- Use streaming for better user experience.
- Keep an eye on token limits and cost.
- Use environment variables for API keys.
- Abstract model selection so providers can be switched easily.
- Use chat models for most conversational applications.
- Tune parameters based on the use case.

## 10. Key Takeaways

- LangChain supports multiple LLM providers.
- Chat models are preferred for many modern applications.
- Models can be switched without rewriting the entire application.
- Parameters such as temperature and token limits affect behavior.
- Streaming enables real-time responses.

> Models are just the beginning. The real power comes from how you use them.

---

# 5. Prompts + Prompt Templates

## 1. What are Prompts?

- A prompt is the input text given to an LLM to get a response.
- It can be a simple question or a detailed instruction.
- Prompt quality directly affects output quality.
- Good prompts are clear, specific and provide enough context.

> A good prompt turns a general model into a useful assistant.

## 2. Types of Prompts

| Type | Description |
|---|---|
| Zero Shot | Direct instruction without examples |
| Few Shot | Provide examples in the prompt |
| Chain of Thought | Ask the model to reason step by step |
| Role Based | Assign a specific role |
| Instruction Based | Give clear task instructions |
| Context Based | Provide background context |
| Multimodal | Use text + images for multimodal models |

## 3. Prompt vs Prompt Template

### Simple Prompt

```text
Explain what MLOps is in simple words.
```

### Prompt Template

A reusable prompt containing placeholders:

```python
from langchain.prompts import PromptTemplate

template = PromptTemplate(
    input_variables=["topic"],
    template="Explain {topic} in simple words."
)

prompt = template.format(topic="MLOps")
print(prompt)
```

> Prompt templates let you reuse and parameterize prompts.

## 4. Creating a Prompt Template

```python
from langchain.prompts import PromptTemplate

template = PromptTemplate(
    input_variables=["name", "topic"],
    template="You are a helpful assistant. Explain {topic} to {name}."
)

prompt = template.format(
    name="Nikhil",
    topic="LangChain"
)

print(prompt)
```

## 5. ChatPromptTemplate

```python
from langchain.prompts import ChatPromptTemplate

template = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful AI assistant."),
    ("user", "Explain {topic} in simple words.")
])

prompt = template.format_messages(topic="MLOps")
print(prompt)
```

Chat prompts can define system, user and assistant-style messages.

## 6. Few-Shot Prompting

Few-shot prompting provides examples before the actual question.

```python
from langchain.prompts import FewShotPromptTemplate, PromptTemplate

examples = [
    {"input": "2 + 2", "output": "4"},
    {"input": "3 + 5", "output": "8"}
]

example_prompt = PromptTemplate(
    input_variables=["input", "output"],
    template="Question: {input}\nAnswer: {output}"
)

prompt = FewShotPromptTemplate(
    examples=examples,
    example_prompt=example_prompt,
    input_variables=["input"],
    suffix="Question: {input}",
    prefix="Answer the following:"
)

print(prompt.format(input="10 + 5"))
```

## 7. Best Practices for Prompting

- Be clear and specific.
- Provide context.
- Use role-based instructions.
- Break complex tasks into smaller steps.
- Use examples when useful.
- Control output format such as JSON or bullet points.
- Set constraints for length, style and tone.
- Iterate and refine prompts.

> Good prompts save time and reduce unnecessary iterations.

## 8. Common Prompt Templates

| Template | Use Case |
|---|---|
| Summarization | Summarize long text |
| Q&A | Answer questions from context |
| Code Generation | Generate code from a description |
| Data Extraction | Extract structured data such as JSON |
| Explanation | Explain complex concepts |
| Translation | Translate text to another language |
| Creative Writing | Generate blogs, stories, etc. |
| Classification | Classify text into categories |

## 9. Key Takeaways

- Prompts are the input to LLMs.
- Prompt templates make prompts reusable.
- Use `ChatPromptTemplate` for chat models.
- Experiment with different prompting techniques.
- Good prompting improves output quality.
- Iterate and test prompts against real examples.

> Prompting is a skill. The better you get at it, the more powerful AI becomes.

---

# 6. Messages + Message History

## 1. What are Messages?

Messages are the standard format for communicating with chat models in LangChain.

They represent the role and content of each message.

Common roles include:

- System
- Human
- AI
- Tool
- Function

> Messages make conversations structured, consistent and powerful.

## 2. Types of Messages

| Message Type | Class | Use Case |
|---|---|---|
| System Message | `SystemMessage` | Set behavior and instructions |
| Human Message | `HumanMessage` | User input |
| AI Message | `AIMessage` | Model response |
| Tool Message | `ToolMessage` | Response from a tool |
| Function Message | `FunctionMessage` | Function-calling responses |
| Chat Message | `ChatMessage` | Custom role messages |

## 3. Creating Messages

```python
from langchain.schema import (
    SystemMessage,
    HumanMessage,
    AIMessage,
    ToolMessage
)

messages = [
    SystemMessage(content="You are a helpful AI assistant."),
    HumanMessage(content="What is MLOps?"),
    AIMessage(content="MLOps stands for Machine Learning Operations.")
]
```

Use message objects to build structured conversations.

## 4. Passing Messages to a Chat Model

```python
from langchain.chat_models import ChatOpenAI
from langchain.schema import HumanMessage, SystemMessage

chat = ChatOpenAI(model="gpt-3.5-turbo")

messages = [
    SystemMessage(content="You are a helpful assistant."),
    HumanMessage(content="Explain LangChain in simple words.")
]

response = chat.invoke(messages)
print(response.content)
```

> Pass a list of message objects instead of a single string.

## 5. ChatMessage (Custom Role)

```python
from langchain.schema import ChatMessage

messages = [
    ChatMessage(
        role="developer",
        content="You are an expert in AI."
    ),
    ChatMessage(
        role="user",
        content="Give me the best resources."
    )
]
```

Use `ChatMessage` to define custom roles beyond standard system, human and assistant roles.

## 6. Message History (In Memory)

```python
from langchain.memory import ChatMessageHistory

history = ChatMessageHistory()

history.add_user_message("Hello!")
history.add_ai_message("Hi! How can I help you?")
history.add_user_message("Tell me about MLOps.")

for msg in history.messages:
    print(msg.type, msg.content)
```

> `ChatMessageHistory` stores conversation messages in memory.

## 7. Using Message History with a Chain

```python
from langchain.chains import ConversationChain
from langchain.chat_models import ChatOpenAI
from langchain.memory import ChatMessageHistory

chat = ChatOpenAI(model="gpt-3.5-turbo")
memory = ChatMessageHistory()

chain = ConversationChain(
    llm=chat,
    memory=memory,
    verbose=True
)

chain.run("Hi, my name is Nikhil.")
chain.run("What is my name?")
```

## 8. Other Memory Options

| Memory Type | Description |
|---|---|
| `ChatMessageHistory` | In-memory message storage |
| `ConversationBufferMemory` | Stores all conversation history as text |
| `ConversationBufferWindowMemory` | Stores the last `k` messages |
| `ConversationSummaryMemory` | Summarizes old messages |
| `ConversationSummaryBufferMemory` | Hybrid summary + buffer |
| `VectorStoreRetrieverMemory` | Stores messages in a vector store for long-term retrieval |

## 9. Key Takeaways

- Messages are the standard format for chat models.
- Use `SystemMessage`, `HumanMessage`, `AIMessage` and `ToolMessage` as needed.
- Message history maintains context across multiple turns.
- LangChain provides several memory implementations.
- Structured messages lead to more reliable conversations.

---

# 7. Chains + LCEL

## 1. What are Chains?

- Chains are sequences of components connected to perform a task.
- They combine multiple steps such as prompting, calling a model and parsing output.
- Chains help build complex workflows in a modular way.
- In LangChain, chains can be created using traditional chain classes or newer LCEL patterns.

> Chains turn multiple steps into one simple pipeline.

## 2. Why LCEL?

**LCEL = LangChain Expression Language**

- Makes chains more modular and powerful.
- Uses the pipe operator (`|`) to connect components.
- More readable and easier to debug.
- Supports streaming.
- Supports parallel execution and complex workflows.
- Works with prompts, models, parsers, retrievers and other components.

> LCEL makes building chains as easy as writing a simple expression.

## 3. Basic LCEL Chain

```python
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

prompt = ChatPromptTemplate.from_template(
    "You are a helpful assistant. Explain {topic} in simple words."
)

model = ChatOpenAI(model="gpt-3.5-turbo")
parser = StrOutputParser()

chain = prompt | model | parser

response = chain.invoke({"topic": "LangChain"})
print(response)
```

> Use `|` to connect components in LCEL.

## 4. Chain Components

| Component | Description |
|---|---|
| PromptTemplate | Creates a prompt from a template |
| ChatModel | LLM that generates the response |
| OutputParser | Parses and formats model output |
| Retriever | Fetches relevant documents |
| Tool | External tool or API |
| Runnable | Any component that can be run |
| Lambda | Custom function in a chain |
| RunnablePassthrough | Passes input through unchanged |

These components can be combined using LCEL.

## 5. Different Chain Examples

### A. Simple LLM Chain

```python
chain = prompt | model | parser
```

Flow:

```text
prompt → model → parser
```

### B. Chain with Retriever (RAG)

```python
chain = {
    "context": retriever,
    "question": RunnablePassthrough()
} | prompt | model | parser
```

### C. Chain with Custom Function

```python
chain = (
    prompt
    | model
    | (lambda x: x.upper())
    | parser
)
```

## 6. LCEL Features

- **Composable:** Connect components with `|`.
- **Readable:** Clean and intuitive syntax.
- **Flexible:** Supports branching, parallel execution and custom functions.
- **Streaming:** Easy to enable streaming.
- **Async Support:** Works asynchronously.
- **Integration:** Works with LangChain retrievers and other components.
- **Debuggable:** Can use configuration and tracing.

> LCEL gives more control with less code.

## 7. Advanced LCEL Patterns

### Parallel Execution

```python
chain = {
    "summary": prompt1 | model | parser,
    "translation": prompt2 | model | parser
}
```

### Conditional Chain / RunnableBranch

```python
from langchain_core.runnables import RunnableBranch

chain = RunnableBranch(
    (lambda x: "math" in x["topic"], math_chain),
    (lambda x: True, general_chain)
)
```

LCEL supports complex workflows with minimal code.

## 8. Chain Flow Diagram

### Simple Chain

```text
Input
  ↓
Prompt Template
  ↓
LLM / Model
  ↓
Output Parser
  ↓
Final Response
```

### RAG Chain

```text
User Question
      ↓
  Retriever ← Documents
      ↓
Prompt Template
      ↓
     LLM
      ↓
 Output Parser
      ↓
   Response
```

## 9. Key Takeaways

- Chains help build multi-step workflows.
- LCEL is the recommended way to compose many modern LangChain components.
- Use `|` to connect prompts, models, retrievers, parsers and functions.
- LCEL supports streaming, branching and parallel execution.
- Start with simple chains and gradually introduce complex workflows.

> Simple chains today, intelligent applications tomorrow.

---

# 8. Output Parsers + Structured Output

## 1. What are Output Parsers?

- Output parsers convert raw text from an LLM into a structured format such as JSON, Pydantic models or lists.
- They help maintain consistent and reliable outputs.
- Useful when integrating LLM output with applications.
- LangChain provides built-in parsers and also allows custom parsers.

> Output parsers turn unstructured text into usable data.

## 2. Why Structured Output?

- LLMs can generate different formats each time.
- Structured output improves consistency.
- Helps in automation and integration with other systems.
- Useful for APIs, databases, agents and production applications.
- Reduces the need for complex post-processing.

> Structured output = Reliability + Consistency + Automation.

## 3. Common Output Parsers

| Parser | Description |
|---|---|
| `StrOutputParser` | Returns output as a plain string |
| `CommaSeparatedListOutputParser` | Parses comma-separated lists |
| `JsonOutputParser` | Parses JSON output |
| `PydanticOutputParser` | Parses output into a Pydantic model |
| `StructuredOutputParser` | Parses based on a defined schema |
| `EnumOutputParser` | Parses output into an enum value |
| `DatetimeOutputParser` | Parses date/time values |
| `OutputFixingParser` | Attempts to fix invalid parsing output |

Choose the parser based on the expected output format.

## 4. StrOutputParser

```python
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser

model = ChatOpenAI(model="gpt-3.5-turbo")
parser = StrOutputParser()

chain = model | parser

response = chain.invoke("What is MLOps?")
print(response)
```

Returns output as a simple string.

## 5. JsonOutputParser

```python
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import JsonOutputParser

model = ChatOpenAI(model="gpt-3.5-turbo")
parser = JsonOutputParser()

chain = model | parser

response = chain.invoke(
    "Return a JSON with keys: name, age, role for a software engineer."
)

print(response)
```

Parses the model output into JSON-like structured data.

## 6. PydanticOutputParser

```python
from pydantic import BaseModel, Field
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import PydanticOutputParser

class Person(BaseModel):
    name: str = Field(description="Name of the person")
    age: int = Field(description="Age of the person")
    role: str = Field(description="Role of the person")

parser = PydanticOutputParser(pydantic_object=Person)

model = ChatOpenAI(model="gpt-3.5-turbo")

chain = model | parser

response = chain.invoke(
    "Tell me about a software engineer."
)

print(response)
```

Parses output into a typed Pydantic model with validation.

## 7. StructuredOutputParser

```python
from langchain.output_parsers import (
    StructuredOutputParser,
    ResponseSchema
)

response_schemas = [
    ResponseSchema(
        name="name",
        description="Name of person"
    ),
    ResponseSchema(
        name="skills",
        description="List of skills"
    ),
    ResponseSchema(
        name="experience",
        description="Years of experience"
    )
]

parser = StructuredOutputParser.from_response_schemas(
    response_schemas
)

format_instructions = parser.get_format_instructions()

response = model.invoke(
    f"Tell me about a data scientist.\n{format_instructions}"
)

print(parser.parse(response.content))
```

> Define a custom schema for structured output.

## 8. OutputFixingParser

Used when an LLM produces output that does not match the expected format.

```python
from langchain.output_parsers import OutputFixingParser

base_parser = JsonOutputParser()

parser = OutputFixingParser.from_llm(
    parser=base_parser,
    llm=model
)

response = parser.parse(
    '{"name": "Tapan", "skills": ["Python",]}'
)

print(response)
```

> It attempts to automatically fix common formatting errors and parse the output.

## 9. Real-World Use Cases

- Extract information from documents.
- Build APIs with LLMs.
- Store structured data in databases.
- Process agent/tool outputs.
- Form filling and data extraction.
- Automation and reporting.
- Integrating LLMs with external systems.

### Pro Tips

- Always give clear format instructions.
- Use Pydantic models for type safety.
- Handle parsing errors gracefully.
- Test with different inputs.
- Use `OutputFixingParser` when appropriate.
- Validate structured output before using it downstream.

## 10. Key Takeaways

- Output parsers convert LLM output into structured data.
- Choose the parser based on the required output.
- Structured output is important for real-world applications.
- Pydantic output is useful for validation and type safety.
- OutputFixingParser can handle parsing errors.
- Structured output enables reliable, consistent and automated workflows.

> Structured output today, smarter applications tomorrow.

---

# 9. Embeddings + Vector Stores

## 1. What are Embeddings?

- Embeddings convert text, images or other data into high-dimensional numerical vectors.
- These vectors capture meaning and semantic similarity.
- Similar content gets similar vectors.
- Embeddings allow machines to understand and compare content beyond exact keyword matching.
- Useful for search, retrieval, clustering and recommendation systems.

> Embeddings turn words into numbers that capture meaning.

## 2. How Embeddings Work

A model such as OpenAI or Hugging Face converts text into a vector.

```text
"Machine learning is amazing."
             ↓
       Embedding Model
             ↓
[0.12, -0.34, 0.56, ...]
```

Similar meaning:

```text
Similar meaning → Similar vectors
Different meaning → Distant vectors
```

Vectors can be compared using similarity metrics such as cosine similarity.

## 3. Generating Embeddings

```python
from langchain_openai import OpenAIEmbeddings

embeddings = OpenAIEmbeddings(
    model="text-embedding-3-small"
)

text = "Machine learning is amazing."

vector = embeddings.embed_query(text)

print(len(vector))
print(vector[:5])
```

The exact dimensionality depends on the embedding model/configuration.

Other options include Hugging Face, Cohere and other embedding providers.

## 4. Common Embedding Models

| Provider | Model | Dimension / Characteristic | Use Case |
|---|---|---|---|
| OpenAI | `text-embedding-3-small` | General-purpose | General use |
| OpenAI | `text-embedding-3-large` | High quality | Higher accuracy |
| Hugging Face | `all-MiniLM-L6-v2` | Lightweight | Fast/local retrieval |
| Hugging Face | `multilingual-e5-large` | Multilingual | Multilingual search |
| Google | `text-embedding-004` | Multimodal-capable ecosystem | Search/retrieval |
| Instructor | `instructor-large` | Instruction-aware | Better contextual embeddings |
| BGE | `bge-large-en` | High performance | Retrieval |

Choose based on use case, accuracy, latency and cost.

## 5. What are Vector Stores?

- Vector stores save embedding vectors together with their metadata.
- They allow fast similarity search over large datasets.
- They are heavily used in RAG to find relevant context.
- Popular vector stores include FAISS, Chroma, Pinecone, Weaviate, Qdrant and Milvus.

> Vector stores are like databases for embeddings, optimized for similarity search.

## 6. Using a Vector Store: Chroma Example

```python
from langchain_community.document_loaders import TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import Chroma

loader = TextLoader("data.txt")
docs = loader.load()

splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=50
)

chunks = splitter.split_documents(docs)

embeddings = OpenAIEmbeddings(
    model="text-embedding-3-small"
)

vectorstore = Chroma.from_documents(
    documents=chunks,
    embedding=embeddings,
    persist_directory="chroma_db"
)

print("Documents stored in Chroma!")
```

This loads documents, splits them, creates embeddings and stores them in Chroma.

## 7. Similarity Search

```python
query = "What is machine learning?"

results = vectorstore.similarity_search(
    query,
    k=3
)

for doc in results:
    print(doc.page_content)
    print(doc.metadata)
```

Returns the most relevant documents based on semantic similarity.

## 8. Vector Similarity Metrics

| Metric | Description | Typical Use |
|---|---|---|
| Cosine Similarity | Measures angle between vectors | Most common for text |
| Euclidean Distance | Straight-line distance | Numerical data |
| Dot Product | Measures vector alignment | Used by some models |
| Manhattan Distance | Sum of absolute differences | Less common |

Cosine similarity is commonly used for text embeddings.

## 9. Real-World Applications

- Semantic search over documents, websites and FAQs.
- RAG for chatbots and AI assistants.
- Recommendation systems.
- Clustering and classification.
- Image and video search.
- Enterprise knowledge search.
- Personalized content and recommendations.

## 10. Key Takeaways

- Embeddings convert data into numerical vectors.
- Vector stores enable fast semantic search.
- They are heavily used in RAG and real-world AI systems.
- Choose embedding models based on accuracy, cost and latency.
- Understand similarity metrics.
- Embeddings + vector stores unlock powerful applications.

> Embeddings give meaning to data. Vector stores give it memory.

---

# 10. Document Loaders + Text Splitters

## 1. What are Document Loaders?

- Document loaders bring data into LangChain from different sources such as PDF, TXT, web pages, Notion, YouTube and more.
- They convert external data into a standard `Document` object.
- Each document contains page content and metadata.
- LangChain provides many built-in loaders for different file types and platforms.

> Document loaders bring your data into LangChain.

## 2. Document Object Structure

```python
from langchain_core.documents import Document

doc = Document(
    page_content="This is a sample text.",
    metadata={
        "source": "example.pdf",
        "page": 1
    }
)

print(doc.page_content)
print(doc.metadata)
```

Conceptually:

```text
Document = text + metadata
```

## 3. Common Document Loaders

| Loader | Use Case |
|---|---|
| `TextLoader` | Load `.txt` files |
| `PyPDFLoader` | Load PDF files |
| `CSVLoader` | Load CSV files |
| `WebBaseLoader` | Load web pages / URLs |
| `UnstructuredFileLoader` | Load various file types |
| `NotionLoader` | Load data from Notion |
| `YoutubeLoader` | Load YouTube transcripts |
| `DirectoryLoader` | Load multiple files from a folder |

Choose the loader based on your data source.

## 4. Example: Load a PDF

```python
from langchain_community.document_loaders import PyPDFLoader

loader = PyPDFLoader("data/notes.pdf")
docs = loader.load()

print(len(docs))
print(docs[0].page_content[:200])
print(docs[0].metadata)
```

Typically, each PDF page becomes a document object.

## 5. Example: Load a Web Page

```python
from langchain_community.document_loaders import WebBaseLoader

loader = WebBaseLoader("https://example.com")
docs = loader.load()

print(len(docs))
print(docs[0].page_content[:200])
```

Useful for blogs, documentation and public web pages.

## 6. Example: Load Multiple Files

```python
from langchain_community.document_loaders import (
    DirectoryLoader,
    PyPDFLoader
)

loader = DirectoryLoader(
    "data/",
    glob="*.pdf",
    loader_cls=PyPDFLoader
)

docs = loader.load()

print(f"Total documents: {len(docs)}")
```

Loads all matching PDFs from the specified folder.

## 7. What are Text Splitters?

- Text splitters divide large documents into smaller chunks.
- LLMs have context-window limits.
- Splitting helps fit content into the model context.
- Smaller meaningful chunks can improve retrieval quality.
- LangChain provides different splitting strategies depending on the data.

> Split large text into smaller, meaningful chunks.

## 8. Common Text Splitters

| Splitter | Use Case |
|---|---|
| `CharacterTextSplitter` | Simple character-based splitting |
| `RecursiveCharacterTextSplitter` | Hierarchical splitting, common for general text |
| `TokenTextSplitter` | Split based on token count |
| `SentenceTransformersTokenTextSplitter` | Token-based splitting using Sentence Transformers |
| `MarkdownTextSplitter` | Good for Markdown files |
| `HTMLTextSplitter` | Good for HTML content |

`RecursiveCharacterTextSplitter` is commonly used for general-purpose document splitting.

## 9. Example: Split Text into Chunks

```python
from langchain.text_splitter import RecursiveCharacterTextSplitter

text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=200
)

chunks = text_splitter.split_documents(docs)

print(f"Total chunks: {len(chunks)}")
print(chunks[0].page_content[:200])
```

`chunk_size` controls the approximate size of each chunk.

`chunk_overlap` preserves some context between neighboring chunks.

## 10. Chunking Strategies

```text
Large Document
(PDF / Web Page)
       ↓
 Text Splitter
       ↓
 ┌──────────┐
 │ Chunk 1  │
 ├──────────┤
 │ Chunk 2  │
 ├──────────┤
 │ Chunk 3  │
 ├──────────┤
 │   ...    │
 └──────────┘
```

Split the document into smaller chunks for better retrieval and processing.

## 11. Best Practices

- Choose the right loader for your data source.
- Clean and preprocess text if needed.
- Use `RecursiveCharacterTextSplitter` for many general-purpose use cases.
- Set appropriate `chunk_size` and `chunk_overlap`.
- Maintain metadata such as source, page number and document ID.
- Experiment with different splitters.
- Test chunk quality with real RAG, agent and retrieval workloads.

> Good splitting → Better retrieval → Better answers.

## 12. Key Takeaways

- Document loaders bring external data into LangChain.
- Text splitters break large text into smaller chunks for LLMs.
- Use the right loader and splitter for the data source.
- Maintain metadata for better traceability.
- Proper chunking improves retrieval quality and final responses.

> Load the right data. Split it smartly. Build something amazing.

---

## 10. Retrievers + RAG

### 1. What are Retrievers?

-   Retrievers are components that search and fetch relevant documents
    from a data source based on a user query.
-   They convert the query into embeddings and find the most similar
    documents.
-   Used in RAG (Retrieval Augmented Generation) to provide context to
    the LLM.
-   Common retrievers: vector store retrievers, BM25 retrievers, hybrid
    retrievers, etc.

> "Retrievers help LLMs find the right information instead of relying
> only on pretraining."

### 2. What is RAG?

-   RAG (Retrieval Augmented Generation) combines retrieval and
    generation.
-   It first retrieves relevant documents from your data and then passes
    them to an LLM to generate a grounded answer.
-   Useful for domain specific knowledge, chatbots, documentation, and
    real time data.
-   Reduces hallucinations and provides more accurate and up to date
    responses.

> "RAG = Retrieve relevant data + Generate a better answer."

### 3. RAG Architecture (High Level)

``` text
User Query
   ↓
Embeddings (Query)
   ↓
Retriever (Vector Store / BM25 / Hybrid)
   ↓
Relevant Documents (Top K)
   ↓
Prompt (Instructions + Context + Query)
   ↓
LLM (Chat Model)
   ↓
Final Response
```

> Retrieve relevant context and let the LLM generate a grounded and
> accurate answer.

### 4. Types of Retrievers

  -----------------------------------------------------------------------
  Retriever Type          Description             Use Case
  ----------------------- ----------------------- -----------------------
  Vector Store Retriever  Uses embeddings and     Most common for RAG
                          similarity search       

  BM25 Retriever          Keyword based lexical   Good for exact matches
                          search                  

  Hybrid Retriever        Combines vector and     Better recall and
                          keyword search          precision

  Multi Query Retriever   Generates multiple      Complex queries
                          queries for better      
                          recall                  

  Self Query Retriever    Uses LLM to create      Metadata filtering
                          structured queries      
  -----------------------------------------------------------------------

> Choose the right retriever based on your data and user query.

### 5. Example: Vector Store Retriever

``` python
from langchain_community.document_loaders import TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import Chroma

# Load and split documents
loader = TextLoader("data.txt")
docs = loader.load()
splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
split_docs = splitter.split_documents(docs)

# Create vector store
embeddings = OpenAIEmbeddings(model="text-embedding-3-small")
vectorstore = Chroma.from_documents(split_docs, embeddings)
retriever = vectorstore.as_retriever(search_type="similarity", search_kwargs={"k": 4})
```

> Create a vector store and use it as a retriever to fetch similar
> documents.

### 6. Example: RAG Chain

``` python
from langchain.chains import RetrievalQA
from langchain_openai import ChatOpenAI

llm = ChatOpenAI(model="gpt-3.5-turbo")

qa_chain = RetrievalQA.from_chain_type(
    llm=llm,
    retriever=retriever,
    chain_type="stuff",
)

response = qa_chain.invoke({
    "query": "What is machine learning?"
})

print(response["result"])
```

> Combine retriever and LLM to build a simple RAG pipeline.

### 7. Advanced RAG Techniques

-   Hybrid Search (vector + keyword)
-   Re-ranking (improves relevance of results)
-   Query Expansion (generate multiple queries)
-   Self Query Retriever (LLM powered filtering)
-   Metadata Filtering (filter by source, date, etc.)
-   Context Compression (remove irrelevant content)
-   Multi hop Retrieval (for complex questions)
-   Agentic RAG (use agents for tool based retrieval)

> Use advanced techniques to improve retrieval quality and answer
> accuracy.

### 8. Evaluation Metrics

  -----------------------------------------------------------------------
  Metric                  Description             Use Case
  ----------------------- ----------------------- -----------------------
  Recall                  How many relevant       Check coverage
                          documents were          
                          retrieved               

  Precision               How many retrieved docs Check relevance
                          are actually relevant   

  MRR                     Mean Reciprocal Rank    Best match position

  Hit Rate                Whether relevant doc is Simple evaluation
                          in top K                

  Answer Relevance        Quality of final LLM    End to end check
                          answer                  
  -----------------------------------------------------------------------

> Evaluate both retrieval and final answer for better RAG systems.

### 9. Real World Use Cases

-   Chatbots on company documentation
-   Q&A on PDFs, websites, and knowledge bases
-   Customer support bots
-   Research assistants (papers, articles)
-   Enterprise search across internal data
-   Legal, medical, and finance domain applications
-   Personal knowledge management (notes, docs)

### 10. Key Takeaways

-   Retrievers fetch relevant information from your data.
-   RAG combines retrieval and generation for better answers.
-   Choose the right retriever and use advanced techniques for better
    results.
-   Evaluate your system using proper metrics.
-   RAG reduces hallucinations and enables real world applications.

> Right information + Right model = Real impact.

------------------------------------------------------------------------

# 12. Tools + Tool Calling

### 1. What are Tools?

-   Tools are external functions, APIs or services that LLMs can use to
    perform actions beyond just generating text.
-   They allow the model to interact with the real world (search the
    web, get live data, run code, query databases, etc.).
-   In LangChain, tools are defined with a name, description and a
    function to execute.
-   Tools make LLMs more useful, accurate and up to date.

> Tools turn LLMs from a text generator into an action taker.

### 2. Why Tool Calling?

-   LLMs alone don't have real time information or access to external
    systems.
-   Tool calling allows the model to decide when to use a tool to get
    the required information.
-   Helps in building more reliable and factual applications.
-   Useful for tasks like search, calculations, booking, database
    queries, automation, etc.

> Tool calling = LLM decides + calls the right tool + gets the result +
> gives a final answer.

### 3. How Tool Calling Works?

``` text
User Query
    ↓
LLM (Decides to use a tool)
    ↓
Tool Execution (Call external API / function)
    ↓
Tool Result (Return data to LLM)
    ↓
Final Response (LLM generates answer using result)
```

### 4. Defining a Tool (Example)

``` python
from langchain.tools import tool

@tool
def get_weather(city: str) -> str:
    """Get current weather for a city."""
    # In real case, call a weather API
    return f"The current weather in {city} is sunny with 32°C."
```

> A tool has a name, description, and a function that returns a result.

### 5. Using Tools with an LLM

``` python
from langchain_openai import ChatOpenAI
from langchain.agents import initialize_agent, Tool

llm = ChatOpenAI(model="gpt-3.5-turbo")

tools = [get_weather]

agent = initialize_agent(
    tools=tools,
    llm=llm,
    agent="zero-shot-react-description",
    verbose=True
)

response = agent.invoke("What's the weather in Delhi?")
print(response)
```

> Agent uses the tool when needed and returns the final answer.

### 6. Types of Tools

  Tool Type       Description                       Example
  --------------- --------------------------------- -----------------------------
  API Tool        Calls external APIs               Weather API, Google Maps
  Search Tool     Search information from the web   Tavily, SerpAPI
  Database Tool   Query databases                   SQL Database
  Python REPL     Execute Python code               Calculations, data analysis
  File Tool       Read / write files                Local file system
  Custom Tool     Your own functions                Business logic

### 7. Tool Calling with Chat Models

``` python
from langchain_openai import ChatOpenAI
from langchain_core.tools import tool

@tool
def add(a: int, b: int) -> int:
    """Add two numbers."""
    return a + b

llm = ChatOpenAI(model="gpt-3.5-turbo")

response = llm.bind_tools([add]).invoke(
    "Add 25 and 17 using the tool"
)

print(response)
```

> Chat models can call tools directly using `bind_tools()`.

### 8. Agent vs Direct Tool Calling

  Feature       Direct Tool Calling       Agents
  ------------- ------------------------- ---------------------------------
  Control       You decide when to call   LLM decides when to call
  Flexibility   Simple and lightweight    Handles complex workflows
  Use Case      Specific, single task     Multi step tasks with reasoning
  Setup         Easier                    Slightly complex
  Best For      Simple integrations       Real world applications

> Use direct tool calling for simple use cases and agents for complex
> workflows.

### 9. Best Practices

-   Write clear and descriptive tool descriptions.
-   Keep tool outputs concise and structured.
-   Handle errors and invalid inputs gracefully.
-   Limit the number of tools to avoid confusion.
-   Use caching where possible to reduce API calls.
-   Validate and sanitize tool inputs.
-   Monitor tool usage and costs.

### 10. Key Takeaways

-   Tools give LLMs real world capabilities.
-   LangChain makes it easy to define and use tools.
-   Tool calling improves accuracy and usefulness of LLM applications.
-   You can use built-in tools or create custom tools.
-   Use direct tool calling or agents depending on the workflow.

> LLMs + Tools = Real World Impact.

------------------------------------------------------------------------

# 13. Agents + Agent Loops

### 1. What are Agents?

-   Agents are AI systems that can understand a goal, plan steps, use
    tools and take actions to complete the task.
-   Unlike simple LLM calls, agents can decide what to do next.
-   They can interact with external tools, APIs, databases, and the real
    world.
-   LangChain provides a framework to build agents easily.

> "Agents turn LLMs from passive answer machines into active problem
> solvers."

### 2. Why Agents?

-   Real world problems often need multiple steps, not just a single
    response.
-   Agents can break complex tasks into smaller steps and execute them.
-   They can use tools like search, calculator, file system, database,
    or custom APIs.
-   Useful for automation, research, booking, data analysis, and many
    real world applications.

> "Agents help you get things done, not just answers."

### 3. How Agents Work?

``` text
User provides a goal
        ↓
Agent understands the goal and creates a plan
        ↓
Agent decides which tools to use
        ↓
Agent calls tools and gets results
        ↓
Agent analyzes the results
        ↓
Agent repeats the loop until the task is completed (or stops)
        ↓
Final Answer
```

> Plan → Act → Observe → Repeat → Final Answer

### 4. Basic Agent Example

``` python
from langchain.agents import initialize_agent, Tool
from langchain_openai import ChatOpenAI

llm = ChatOpenAI(model="gpt-3.5-turbo")

tools = [
    Tool(
        name="Search",
        func=search_tool.run,
        description="Search the web for information"
    )
]

agent = initialize_agent(
    tools=tools,
    llm=llm,
    agent="zero-shot-react-description",
    verbose=True
)

response = agent.invoke("Find latest news about GATE 2027")
print(response)
```

> A simple agent that can use a search tool.

### 5. Types of Agents in LangChain

  -----------------------------------------------------------------------
  Agent Type              Description             Use Case
  ----------------------- ----------------------- -----------------------
  Zero Shot ReAct         Decides tools based on  General purpose tasks
                          description             

  Structured Chat         Works with multiple     Complex tool usage
                          tools and structured    
                          inputs                  

  OpenAI Functions Agent  Uses OpenAI function    When using function
                          calling                 calling models

  Plan and Execute        First creates a plan    Long and complex tasks
                          then executes it        

  Self Ask with Search    Breaks question into    Research and
                          sub questions           information gathering

  Conversational Agent    Maintains chat history  Chatbots with tools
  -----------------------------------------------------------------------

> Choose the right agent type based on your task.

### 6. Agent Loop (ReAct Pattern)

1.  **Thought**: Agent thinks about what to do.
2.  **Action**: Agent calls a tool.
3.  **Observation**: Agent gets the result from the tool.
4.  **Repeat**: Agent decides the next step.
5.  **Finish**: Agent returns the final answer.

#### Example Loop

``` text
Thought: I need to search for the latest GATE 2027 date.
Action: Use search tool.
Observation: Got the result.
Thought: Now summarize the information.
Action: Give final answer.
Final Answer: GATE 2027 will be conducted in February...
```

### 7. Memory in Agents

-   Agents can use memory to remember previous interactions.
-   Useful for multi turn conversations and long tasks.
-   LangChain provides different memory types such as:
    -   ConversationBufferMemory
    -   ConversationBufferWindowMemory
    -   ConversationSummaryMemory
    -   ConversationSummaryBufferMemory
    -   EntityMemory

> Memory helps agents have meaningful longer conversations.

### 8. Custom Tools

-   You can create your own tools for specific use cases.
-   Tools can be Python functions, APIs, database queries, or any custom
    logic.

``` python
@tool
def get_stock_price(symbol: str) -> str:
    """Get the current stock price."""
    # Your logic here
    return f"The current price of {symbol} is ₹2500."
```

``` python
# Use in agent
tools = [get_stock_price]
```

> Custom tools make your agents more powerful and useful.

### 9. Multi Agent Systems

-   You can have multiple agents working together.
-   Each agent can have a specific role (e.g. researcher, planner,
    executor).
-   Useful for complex workflows.

``` text
Planner Agent
    ↓
creates plan
    ↓
Research Agent ─────→ collects information
    ↓
Execution Agent ────→ takes actions
    ↓
Final Answer
```

> Multiple agents can collaborate to solve bigger problems.

### 10. Key Takeaways

-   Agents can plan, use tools and complete complex tasks.
-   Agent loops follow a Plan/Act/Observe/Repeat pattern.
-   LangChain provides many types of agents.
-   You can use memory and custom tools to make agents more powerful.
-   Multi agent systems are useful for real world applications.
-   Agents are the next step toward more autonomous LLM systems.

> "Agents don't just answer questions, they make things happen."

------------------------------------------------------------------------

# 14. Memory + Conversation History

### 1. What is Memory?

-   Memory allows an LLM to remember information from previous
    interactions.
-   It helps maintain context across multiple turns in a conversation.
-   Without memory, each chat is independent and the model forgets
    earlier context.
-   Memory can be short term (within a session) or long term (across
    sessions).
-   Useful for chatbots, assistants, and personalized AI applications.

> "Memory turns a single response model into a real conversational AI."

### 2. Why Memory is Important?

-   Maintains context and continuity.
-   Gives more relevant and accurate responses.
-   Enables natural, human like conversations.
-   Useful for tasks like customer support, personal assistants,
    tutoring, etc.
-   Reduces the need to repeat information.
-   Improves user experience and trust.

> "Good memory = Better context = More helpful and natural
> conversations."

### 3. Types of Memory in LangChain

  ---------------------------------------------------------------------------------
  Memory Type                       Description             Use Case
  --------------------------------- ----------------------- -----------------------
  ConversationBufferMemory          Stores all messages     Simple chatbots

  ConversationBufferWindowMemory    Stores last k messages  Limited context

  ConversationSummaryMemory         Summarizes old messages Long conversations

  ConversationSummaryBufferMemory   Combines buffer +       Balanced approach
                                    summarization           

  EntityMemory                      Remembers entities      Personalized chat
                                    (names, facts)          

  VectorStoreRetrieverMemory        Stores past chats in a  Long term memory /
                                    vector store            cross session
  ---------------------------------------------------------------------------------

> Choose the right memory type based on your use case and conversation
> length.

### 4. Basic Example (ConversationBufferMemory)

``` python
from langchain_openai import ChatOpenAI
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationChain

llm = ChatOpenAI(model="gpt-3.5-turbo")
memory = ConversationBufferMemory()

conversation = ConversationChain(
    llm=llm,
    memory=memory,
    verbose=True
)

conversation.run("Hi, my name is Nikhil.")
conversation.run("What is my name?")  # Remembers!
```

> The model remembers previous messages in the same session.

### 5. Using a Window (Last k Messages)

``` python
from langchain_openai import ChatOpenAI
from langchain.memory import ConversationBufferWindowMemory
from langchain.chains import ConversationChain

llm = ChatOpenAI(model="gpt-3.5-turbo")
memory = ConversationBufferWindowMemory(k=3)

conversation = ConversationChain(
    llm=llm,
    memory=memory,
    verbose=True
)

conversation.run("Message 1")
conversation.run("Message 2")
conversation.run("Message 3")
conversation.run("Message 4")
```

> Keeps only the last k messages to manage token usage.

### 6. Using Summary Memory (Long Chat)

``` python
from langchain_openai import ChatOpenAI
from langchain.memory import ConversationSummaryMemory
from langchain.chains import ConversationChain

llm = ChatOpenAI(model="gpt-3.5-turbo")
memory = ConversationSummaryMemory(llm=llm)

conversation = ConversationChain(
    llm=llm,
    memory=memory,
    verbose=True
)

conversation.run("Explain what is machine learning.")
conversation.run("Now what we discussed so far?")
```

> Summarizes older messages to keep important context and save tokens.

### 7. Entity Memory (Remember Key Facts)

``` python
from langchain_openai import ChatOpenAI
from langchain.memory import ConversationEntityMemory
from langchain.chains import ConversationChain

llm = ChatOpenAI(model="gpt-3.5-turbo")

memory = ConversationEntityMemory(llm=llm)

conversation = ConversationChain(
    llm=llm,
    memory=memory,
    verbose=True
)

conversation.run("My name is Nikhil and I live in Ahmedabad.")
conversation.run("What do I live?")
```

> Automatically extracts and remembers important entities like names,
> places, or facts.

### 8. Storing Conversation History

``` python
from langchain.memory import ChatMessageHistory
from langchain.memory import ConversationBufferMemory

history = ChatMessageHistory()
history.add_user_message("Hi, I am Nikhil.")
history.add_ai_message("Hello Nikhil!")

memory = ConversationBufferMemory(
    chat_memory=history,
    return_messages=True
)

print(memory.load_memory_variables({}))
```

> You can store, retrieve and manage conversation history manually.

### 9. Best Practices

-   Choose the right memory type for your use case.
-   Use summarization for long conversations.
-   Limit context window to avoid high token usage.
-   Persist memory in a database for long term use (e.g. Redis, MongoDB,
    or Vector Store).
-   Combine memory with retrieval (RAG) for better results.
-   Handle sensitive data and provide an option to clear chat history.
-   Test how memory affects response quality.

### 10. Key Takeaways

-   Memory helps LLMs maintain context across turns.
-   Different memory types solve different problems.
-   Use window or summary memory for long conversations.
-   Use summarization and external storage for long term memory.
-   A well designed memory system makes user experience much better.

> "Remember the past. Build a better future."

------------------------------------------------------------------------

# 15. Callbacks + Streaming

### 1. What are Callbacks?

-   Callbacks are functions that get called during the execution of a
    LangChain application.
-   They help you track what is happening inside the pipeline (start,
    end, error, intermediate steps, etc.).
-   Useful for logging, monitoring, debugging and custom actions.
-   LangChain provides a callback system to hook into different events.

> "Callbacks give you visibility and control over the LLM execution
> flow."

### 2. What is Streaming?

-   Streaming means getting the LLM response token by token instead of
    waiting for the full response.
-   It reduces perceived latency and improves user experience.
-   Useful for chat applications, long responses, and real time
    interfaces.
-   LangChain supports streaming out of the box with callbacks or direct
    streaming methods.

> "Streaming makes AI responses feel faster and more interactive."

### 3. Callback Events in LangChain

  -----------------------------------------------------------------------
  Event                   When it is Called       Use Case
  ----------------------- ----------------------- -----------------------
  on_llm_start            When LLM starts running Log input, start time

  on_llm_new_token        When a new token is     Streaming, live display
                          generated               

  on_llm_end              When LLM finishes       Log output, stop time

  on_chain_start          When a chain starts     Log chain execution

  on_chain_end            When a chain ends       Get final result

  on_tool_start           When a tool starts      Log tool usage

  on_tool_end             When a tool ends        Log tool result

  on_error                When an error occurs    Handle errors
  -----------------------------------------------------------------------

> Use callbacks to monitor, debug and customize the behavior of your
> application.

### 4. Simple Callback Example

``` python
from langchain.callbacks.base import BaseCallbackHandler
from langchain_openai import ChatOpenAI

class MyHandler(BaseCallbackHandler):

    def on_llm_start(self, serialized, prompts, **kwargs):
        print("LLM started")

    def on_llm_new_token(self, token, **kwargs):
        print(token, end="", flush=True)

    def on_llm_end(self, response, **kwargs):
        print("LLM ended")

llm = ChatOpenAI(
    model="gpt-3.5-turbo",
    callbacks=[MyHandler()]
)

llm.invoke("Explain LangChain")
```

> Callbacks let you hook into different stages of LLM execution.

### 5. Streaming Example

``` python
from langchain_openai import ChatOpenAI

llm = ChatOpenAI(
    model="gpt-3.5-turbo",
    streaming=True
)

response = llm.invoke("Tell me a story about space.")

for chunk in response:
    print(chunk, end="", flush=True)
```

> Another way is using callbacks to stream the response.

### 6. Streaming with Chains

``` python
from langchain.chains import LLMChain
from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate

prompt = PromptTemplate(
    input_variables=["topic"],
    template="Explain {topic} in detail."
)

llm = ChatOpenAI(
    model="gpt-3.5-turbo",
    streaming=True
)

chain = LLMChain(llm=llm, prompt=prompt)
chain.invoke({"topic": "Artificial Intelligence"})
```

> Streaming also works with chains, agents and other LangChain
> components.

### 7. Practical Use Cases

-   Display real time responses in chat applications.
-   Track token usage and cost.
-   Debug and log LLM behavior.
-   Show progress in long running tasks.
-   Monitor tool calls or agents.
-   Build better user experience with live output.
-   Integrate with logging tools (LangSmith, Console, Custom Logs).

> Callbacks and streaming make your application more transparent and
> user friendly.

### 8. Tips and Best Practices

-   Use callbacks for logging and monitoring.
-   Use streaming for better user experience.
-   Handle errors in callbacks.
-   Avoid heavy processing inside callback methods.
-   Use LangSmith for advanced tracing.
-   Combine callbacks with tools and agents.
-   Test with different models and providers.

> Keep it simple, light and focus on useful information.

### 9. Key Takeaways

-   Callbacks allow you to track and customize the execution flow.
-   Streaming provides real time, token by token responses.
-   Both are useful for debugging, monitoring and building interactive
    applications.
-   Callbacks provide built in callback handlers and easy streaming
    support.
-   Use them to build more reliable, transparent and user friendly AI
    applications.

> "More visibility. Better control. Better AI apps."

------------------------------------------------------------------------

# 16. LangGraph Fundamentals

### 1. What is LangGraph?

-   LangGraph is a framework by LangChain for building stateful, multi
    step and controllable AI agents using graphs.
-   It allows you to define workflows where nodes perform functions (LLM
    calls, tools, logic) and edges control the flow.
-   Unlike simple chains, LangGraph maintains state across steps and
    supports loops, branching and human in the loop.
-   Useful for complex agents, multi agent systems and real world
    workflows.

> "LangGraph turns linear prompts into powerful, stateful workflows."

### 2. Key Concepts

-   **Graph:** A collection of nodes and edges.
-   **Node:** A function that takes the state, performs an action and
    returns updated state.
-   **Edge:** Defines which node to run next.
-   **State:** Shared dictionary that stores data across the workflow.
-   **START and END:** Special nodes to mark the beginning and ending of
    a graph.
-   **Conditional Edges:** Decide the next node based on state or
    output.

> "Nodes do the work, edges decide the flow, state keeps the memory."

### 3. Basic Architecture

``` text
START
  ↓
Node 1
(LLM / Tool / Logic)
  ↓
Condition?
 ↙       ↘
Yes       No
 ↓         ↓
Node 2    Node 3
(Next)    (Alternative)
 ↘       ↙
   END
```

> A graph defines how your agent thinks, acts and moves between steps.

### 4. Simple LangGraph Example

``` python
from langgraph.graph import StateGraph, START, END
from typing import TypedDict

class AgentState(TypedDict):
    question: str
    answer: str

def llm_node(state: AgentState):
    from langchain_openai import ChatOpenAI

    llm = ChatOpenAI(model="gpt-3.5-turbo")
    response = llm.invoke(state["question"])

    return {"answer": response.content}

graph = StateGraph(AgentState)

graph.add_node("llm", llm_node)
graph.add_edge(START, "llm")
graph.add_edge("llm", END)

app = graph.compile()

result = app.invoke({"question": "What is LangGraph?"})
print(result)
```

> A minimal LangGraph with one node.

### 5. State Management

-   State is a shared dictionary that flows through all nodes.
-   Each node reads from the state, performs some action and returns an
    updated state.
-   You can define custom state schemas using TypedDict, Pydantic or
    simple dictionaries.
-   State helps maintain context, track progress and pass data between
    steps.

``` python
from typing import TypedDict

class AgentState(TypedDict):
    question: str
    answer: str
    steps: int
```

> State keeps your agent organized and consistent.

### 6. Conditional Edges (Branching)

-   Conditional edges allow the graph to decide the next node based on
    the current state.
-   Useful for decision making, retries, tool use and multi step
    reasoning.
-   The function can return the next node name based on logic.

``` python
def decide_next(state: AgentState):
    if "error" in state:
        return "handle_error"
    elif state.get("steps", 0) < 3:
        return "continue"
    else:
        return "end"

graph.add_conditional_edges(
    "llm",
    decide_next,
    {
        "handle_error": "error_node",
        "continue": "llm",
        "end": END
    }
)
```

> Branching makes your agent smarter and more flexible.

### 7. Loops and Iterations

-   LangGraph supports loops to repeat tasks until a condition is met.
-   Useful for retry mechanisms, self improvement and multi step
    reasoning.
-   You can create loops to send the flow back to a previous node.

``` python
def check_retry(state: AgentState):
    if state.get("steps", 0) < 3:
        return "llm"  # loop back
    return END
```

> Loops help your agent think, refine and get better results.

### 8. Human in the Loop

-   You can add human input at any step in the graph.
-   Useful for approval, clarification or sensitive actions.
-   Pause the graph, get human feedback and then continue.

``` python
def human_input(state: AgentState):
    user_feedback = input("Please review and provide input: ")
    return {"human_feedback": user_feedback}

graph.add_node("human_input", human_input)
```

> Humans + AI = Better and safer decisions.

### 9. Practical Use Cases

-   Multi step research agents
-   Customer support workflows
-   Content generation with review
-   Tool using agents (search, calculator, APIs)
-   Multi agent systems
-   Data analysis pipelines
-   Autonomous AI assistants
-   Complex decision making workflows

> LangGraph is ideal for real world agent applications.

### 10. Key Takeaways

-   LangGraph helps build stateful and controllable agent workflows.
-   Understand nodes, edges and state.
-   Use conditional edges for dynamic workflows.
-   Supports loops and human in the loop.
-   State helps maintain context and memory across steps.
-   Great for complex, real world agent applications.
-   Start small, test well and then scale.

> "From simple graphs to powerful agents, LangGraph gives you control."

------------------------------------------------------------------------

# 17. Multi Agent Systems + Workflows

### 1. What are Multi Agent Systems?

-   A system where multiple AI agents work together to solve complex
    tasks.
-   Each agent has a specific role, goal and tools.
-   Agents can communicate, collaborate and take actions independently.
-   Useful for real world problems that need multiple skills like
    research, planning and execution.
-   LangChain and LangGraph make it easy to build multi agent systems.

> "Multiple agents working together achieve more than a single agent."

### 2. Why Use Multi Agent Systems?

-   Break complex problems into smaller tasks.
-   Each agent can focus on a specific role.
-   Improves accuracy and quality of results.
-   Helps in parallel execution and faster completion.
-   Useful for research, analysis, content creation, data processing and
    automation.
-   Mimics real world collaboration.

> "Right agents for the right tasks lead to better results."

### 3. Common Architectures

#### Sequential

``` text
Agent 1
   ↓
Agent 2
   ↓
Agent 3
```

Agents work one after another.

#### Supervisor

``` text
        Supervisor Agent
        /      |      \
    Agent 1  Agent 2  Agent 3
```

A master agent decides and assigns tasks to other agents.

#### Collaborative

``` text
Agent 1 ↔ Agent 2 ↔ Agent 3
```

Agents communicate and work together.

### 4. Simple Multi Agent Example

``` python
from langchain_openai import ChatOpenAI
from langchain.agents import initialize_agent, Tool

llm = ChatOpenAI(model="gpt-3.5-turbo")

def search(query: str) -> str:
    return "Search results for: " + query

def summarize(text: str) -> str:
    return "Summary: " + text[:100]

tools = [search, summarize]

agent = initialize_agent(
    tools,
    llm,
    agent="zero-shot-react-description"
)

response = agent.invoke("Search and summarize AI news")
print(response)
```

> Multiple agents can use different tools to complete a task.

### 5. Building with LangGraph

``` python
from langgraph.graph import StateGraph, START, END
from typing import TypedDict

class AgentState(TypedDict):
    task: str
    research: str
    summary: str
    final_answer: str

def research_agent(state: AgentState):
    # Agent 1 - Research
    return {"research": "Research data..."}

def summary_agent(state: AgentState):
    # Agent 2 - Summarize
    return {"summary": "Summary of data..."}

def final_agent(state: AgentState):
    # Agent 3 - Final response
    return {"final_answer": "Final response..."}

graph = StateGraph(AgentState)

graph.add_node("research", research_agent)
graph.add_node("summarize", summary_agent)
graph.add_node("final", final_agent)

graph.add_edge(START, "research")
graph.add_edge("research", "summarize")
graph.add_edge("summarize", "final")
graph.add_edge("final", END)

app = graph.compile()
```

> LangGraph helps you define agent workflows using a graph.

### 6. Agent Workflow Example

``` text
User Query
    ↓
Planning Agent
(understands the task and creates a plan)
    ↓
Research Agent
(searches and collects information)
    ↓
Analysis Agent
(analyzes and processes data)
    ↓
Writing Agent
(creates final output)
    ↓
Final Answer
```

> Agents work in a structured workflow to complete complex tasks.

### 7. Real World Use Cases

-   Research and report generation
-   Customer support with multiple agents
-   Data analysis and visualization
-   Content creation (research, write, edit)
-   Automated workflows for business tasks
-   Multi step problem solving
-   Autonomous agents for real world applications

> Multi agent systems can handle complex tasks that are hard for a
> single agent.

### 8. Best Practices

-   Define clear roles and goals for each agent.
-   Use structured workflows.
-   Handle errors and retries.
-   Limit the number of agents to avoid confusion.
-   Use memory for context sharing.
-   Monitor and log agent interactions.
-   Test with real use cases and iterate.

> Good planning and monitoring make multi agent systems reliable.

### 9. Key Takeaways

-   Multi agent systems solve complex problems by breaking them into
    smaller tasks.
-   LangGraph makes it easy to build stateful and controllable agent
    workflows.
-   You can use sequential, supervisor or collaborative architectures.
-   Each agent should have a clear role, tools, memory and goal.
-   Useful for real world applications like research, automation and
    content creation.

> "Agents together turn ideas into action."

------------------------------------------------------------------------

# 18. LangSmith + Tracing + Evaluation

### 1. What is LangSmith?

-   LangSmith is a platform by LangChain for debugging, tracing,
    evaluating and monitoring LLM applications.
-   It helps you understand what is happening inside your chain or
    agent.
-   Provides observability for prompts, LLM calls, tools, agents and
    workflows.
-   Helps find issues, compare runs, improve prompts and measure
    performance.
-   Useful for building reliable and production ready AI applications.

> "LangSmith gives you visibility into your LLM application so you can
> debug, optimize and ship with confidence."

### 2. Why Tracing is Important?

-   Lets you see each step of your application (LLM calls, tool calls,
    prompts, outputs).
-   Helps in debugging errors and unexpected behavior.
-   Provides visibility of the full execution.
-   Shows token usage, latency and cost.
-   Useful for complex chains and agents where multiple steps are
    involved.
-   Makes collaboration easier with shared runs and datasets.

> "If you can't see what your AI is doing, you can't improve it."

### 3. Key Features of LangSmith

  Feature           Description
  ----------------- --------------------------------------------------
  Tracing           Track and visualize each step of execution
  Debugging         Inspect inputs, outputs, prompts and errors
  Evaluation        Measure quality using predefined metrics
  Datasets          Create and manage test datasets
  Experimentation   Compare different prompts, models and chains
  Monitoring        Track performance, errors and latency over time
  Collaboration     Share runs and results with your team
  Integrations      Works with LangChain, OpenAI and other providers

> All in one platform to develop, test and improve your LLM
> applications.

### 4. Basic Setup

Create a LangSmith account at:

``` text
https://smith.langchain.com
```

Get your API key from settings.

Set environment variables:

``` python
import os

os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_API_KEY"] = "your_api_key"
os.environ["LANGCHAIN_PROJECT"] = "my-project"
```

> Now all your LangChain runs will be automatically traced in LangSmith.

### 5. Tracing an LLM Call (Example)

``` python
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage

llm = ChatOpenAI(model="gpt-3.5-turbo")

response = llm.invoke(
    [HumanMessage(content="Explain LangChain in simple words.")]
)

print(response.content)
```

-   This run will appear in your LangSmith project.
-   You can see input, output, tokens, latency and more.

> Run your code and see the trace in LangSmith.

### 6. Tracing Chains and Agents

``` python
from langchain.agents import initialize_agent, Tool
from langchain_openai import ChatOpenAI

def search(query: str) -> str:
    return "Search results for: " + query

llm = ChatOpenAI(model="gpt-3.5-turbo")

agent = initialize_agent(
    tools=[search],
    llm=llm,
    agent="zero-shot-react-description",
    verbose=True
)

agent.invoke("Find latest news about AI")
```

> LangSmith traces every step including tool calls.

### 7. Evaluation in LangSmith

-   Evaluation helps you measure the quality of your LLM outputs.
-   You can use predefined evaluators or create custom evaluators.

#### Common Metrics

  Metric           Description
  ---------------- -------------------------------------
  Relevance        How relevant is the response
  Correctness      Is the answer factually correct
  Helpfulness      Is the response useful
  Coherence        Is the response well structured
  Groundedness     Does it use the given context
  Custom Metrics   Define your own evaluation criteria

> Evaluate. Compare. Improve.

### 8. Datasets and Experiments

-   Create datasets with test examples (question, context, expected
    answer).
-   Run experiments with different prompts, models or configurations.
-   Compare results side by side.
-   Helps you choose the best approach based on real data.

``` python
from langsmith import Client

client = Client()

client.create_dataset(
    dataset_name="my_dataset",
    examples=[
        {
            "input": {"question": "What is RAG?"},
            "output": {"answer": "..."}
        }
    ]
)
```

> Test your ideas on real examples, not just vibes.

### 9. Best Practices

-   Trace everything during development.
-   Use meaningful run names and tags.
-   Create datasets for important use cases.
-   Evaluate regularly and compare results.
-   Monitor token usage and cost.
-   Collaborate with your team using shared projects.
-   Set up alerts for errors or performance issues.
-   Keep iterating based on evaluation results.

### 10. Key Takeaways

-   LangSmith helps you build reliable and high quality LLM
    applications.
-   Tracing gives visibility into every step.
-   Evaluation helps you measure and improve performance.
-   Datasets and experiments make it easy to compare ideas.
-   Essential for real world production deployments.

> "Observe. Evaluate. Iterate. Build Better AI."

------------------------------------------------------------------------

# 19. Security + Guardrails + Production

### 1. Why Security Matters?

-   LLM applications can deal with sensitive data (user information,
    business data, internal documents).
-   They are vulnerable to misuse, prompt injection, data leaks and
    model abuse.
-   Security ensures trust, compliance and safe usage in the real world.
-   Important for both users and businesses that adopt AI responsibly.
-   A secure system protects data, users and your brand reputation.

> "Great AI is not just powerful, it is also safe and trustworthy."

### 2. Common Risks and Threats

-   **Prompt Injection:** Manipulating the model to ignore instructions.
-   **Jailbreaking:** Bypassing safety restrictions.
-   **Data Leakage:** Accidental exposure of sensitive information.
-   **Insecure Tool Usage:** Harmful actions through connected tools.
-   **Adversarial Inputs:** Tricking the model with malicious prompts.
-   **Model Hallucination:** Incorrect or misleading outputs.
-   **Abuse and Misuse:** Spam, harmful content or illegal activities.

> Understand the risks so you can build better protection.

### 3. Guardrails and Mitigations

  -----------------------------------------------------------------------
  Guardrail               What It Does            Example / Tool
  ----------------------- ----------------------- -----------------------
  Input Validation        Checks and filters user Regex, LLM Guard
                          input                   

  Content Moderation      Blocks harmful content  OpenAI Moderation,
                                                  Guardrails

  Prompt Injection        Detects malicious       LLM Guard, NeMo
  Detection               instructions            Guardrails

  Output Filtering        Filters unsafe outputs  Custom filters,
                                                  Moderation APIs

  Tool Permissions        Restricts tool access   Allowlist, role based
                          and actions             access

  Data Privacy            Removes or masks        PII redaction, DLP
                          sensitive data          

  Rate Limiting           Prevents abuse and      API limits, quotas
                          overuse                 

  Audit Logging           Tracks activity for     LangSmith, Cloud Logs
                          security and debugging  
  -----------------------------------------------------------------------

> Guardrails help you control what goes in, what happens inside and what
> comes out.

### 4. Input and Output Guardrails

#### Input Guardrail

``` python
def validate_input(user_input: str) -> str:
    banned_words = ["hack", "ignore", "bypass"]

    for word in banned_words:
        if word in user_input.lower():
            return "Your input contains restricted content."

    return user_input
```

#### Output Guardrail using OpenAI Moderation

``` python
from openai import OpenAI

client = OpenAI()

def check_output(text: str) -> str:
    response = client.moderations.create(input=text)

    if response.results[0].flagged:
        return "Output blocked due to policy violation."

    return text
```

> Validate inputs and filter outputs to keep your application safe.

### 5. Secure Tool Usage

-   Give only required permissions to tools.
-   Use allowlists instead of blocklists where possible.
-   Validate parameters before tool execution.
-   Prevent tools from accessing sensitive systems directly.
-   Log and monitor all tool calls.

``` python
# Example: Allow only specific tools
allowed_tools = ["web_search", "calculator"]

def run_tool(tool_name: str, args: dict):
    if tool_name not in allowed_tools:
        return "Tool not allowed."

    # execute tool safely
    return f"Running {tool_name} with {args}"
```

> Least privilege makes your agents safer and more reliable.

### 6. Deployment and Production

-   Use environment variables for API keys and secrets.
-   Deploy using secure cloud platforms (AWS, GCP, Azure).
-   Enable HTTPS and encryption for data in transit and at rest.
-   Use monitoring and logging.
-   Set up alerts for errors, unusual usage or policy violations.
-   Plan for scalability, high availability and backups.
-   Follow compliance requirements (GDPR, SOC 2, etc.).

``` python
# Example: Load API key from environment
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)
```

> A good deployment is secure, scalable and well monitored.

### 7. Monitoring and Observability

-   Track requests, responses, token usage and latency.
-   Use LangSmith for tracing and debugging.
-   Monitor cost and performance.
-   Set up alerts for anomalies.
-   Review logs to detect misuse or unexpected behavior.
-   Use dashboards for real time monitoring.

> What you monitor, you can improve.

### 8. Compliance and Responsible AI

-   Follow data privacy laws (GDPR, DPDP, etc.).
-   Use data anonymization and redaction.
-   Be transparent about AI usage.
-   Avoid biased or harmful outputs.
-   Keep humans in the loop for critical decisions.
-   Document your system and policies.

> Build AI that is ethical, fair and compliant.

### 9. Best Practices Checklist

-   [ ] Validate and sanitize user inputs
-   [ ] Use content moderation and output filters
-   [ ] Restrict tool permissions with allowlists
-   [ ] Store secrets in environment variables
-   [ ] Enable logging and monitoring
-   [ ] Set rate limits and usage quotas
-   [ ] Plan for scalability and backups
-   [ ] Follow compliance and privacy guidelines
-   [ ] Test for security vulnerabilities
-   [ ] Keep improving based on real world feedback

### 10. Key Takeaways

-   Security, guardrails and production readiness are essential for real
    world AI applications.
-   Protect your users, data and brand reputation.
-   Use guardrails at every layer: input, model, tools and output.
-   Monitor, log and iterate continuously.
-   Follow best practices and compliance requirements.
-   A safe and reliable AI application builds long term trust.
-   Start small, test well and then scale.

> "Safe AI today, a better tomorrow."

------------------------------------------------------------------------

# 20. End to End LangChain RAG + Agent Project

## Build a Real World AI Application Step by Step

### 1. Project Overview

-   Build a real world AI application using LangChain.
-   Combine RAG (Retrieval Augmented Generation) with Agents.
-   Use your own documents (PDFs, Docs, URLs).
-   Let the agent answer questions, summarize content and perform
    actions using tools.
-   Deploy the application with a simple UI and make it production
    ready.

> "A complete hands on project to go from data to intelligent AI."

### 2. Tech Stack

-   Python
-   LangChain
-   LangGraph (optional)
-   OpenAI or any LLM (Groq, Anthropic, etc.)
-   Vector Store (Chroma, FAISS / Pinecone)
-   Document Loaders (PDF, URL, etc.)
-   Streamlit (for UI)
-   Tools (Web Search, Calculator, etc.)
-   Deployment (Docker, Railway, Render, etc.)

#### Main Technologies

``` text
Python
LangChain
OpenAI
Chroma
Streamlit
Docker
Render
GitHub
```

### 3. System Architecture

``` text
Documents
(PDF / URL / etc.)
        ↓
Load & Split
Text Splitter
        ↓
Create
Embeddings
        ↓
Vector Store
(Chroma / ...)
        ↓
Retriever
(similarity search)
        ↓
Agent
(with Tools)
        ↙      ↓       ↘
   Web Search Calculator Custom Tools
                     (API, DB, etc.)
        ↓
       LLM
   (OpenAI / Groq)
        ↓
   Final Answer
```

> RAG gives knowledge. Agent gives actions.

### 4. Load and Process Documents

``` python
from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter

# Load PDF
loader = PyPDFLoader("data/notes.pdf")
docs = loader.load()

# Split documents
splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=200
)

splits = splitter.split_documents(docs)
```

> Load your data and split it into smaller chunks for better retrieval.

### 5. Create Embeddings and Vector Store

``` python
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import Chroma

# Create embeddings
embeddings = OpenAIEmbeddings(
    model="text-embedding-3-small"
)

# Store in Chroma
vectorstore = Chroma.from_documents(
    documents=splits,
    embedding=embeddings,
    persist_directory="chroma_db"
)

# Create retriever
retriever = vectorstore.as_retriever(
    search_type="similarity",
    search_kwargs={"k": 5}
)
```

> Convert your content into vector embeddings and store it in a vector
> database.

### 6. Build RAG Chain

``` python
from langchain.chains import RetrievalQA
from langchain_openai import ChatOpenAI

llm = ChatOpenAI(
    model="gpt-3.5-turbo",
    temperature=0
)

qa_chain = RetrievalQA.from_chain_type(
    llm=llm,
    retriever=retriever,
    chain_type="stuff",
    return_source_documents=True
)

response = qa_chain.invoke({
    "query": "What are the main points from the document?"
})

print(response["result"])
```

> RAG chain answers questions using your documents as the source.

### 7. Add Tools and Create Agent

``` python
from langchain.agents import initialize_agent, Tool
from langchain_openai import ChatOpenAI

search_tool = Tool(
    name="Web Search",
    func=DuckDuckGoSearchRun().run,
    description="Search the web for the latest information"
)

llm = ChatOpenAI(model="gpt-3.5-turbo")

agent = initialize_agent(
    tools=[search_tool],
    llm=llm,
    agent="zero-shot-react-description",
    verbose=True
)

agent.invoke("Search and summarize latest AI news.")
```

> Give your agent tools like web search, calculator, or custom APIs.

### 8. Build a UI with Streamlit

``` python
import streamlit as st

st.set_page_config(
    page_title="RAG Agent",
    page_icon="🤖"
)

st.title("RAG + Agent Assistant")

query = st.text_input(
    "Ask a question about your documents:"
)

if query:
    response = agent.invoke({"input": query})

    st.write(response["output"])

    if "source_documents" in response:
        st.write("### Sources")

        for doc in response["source_documents"]:
            st.write(
                doc.metadata.get("source", "N/A")
            )
```

> Create a simple UI to interact with your RAG Agent and see results in
> real time.

### 9. Deploy and Make it Production Ready

-   Use environment variables for API keys.
-   Use Docker for consistent setup.
-   Add authentication if required.
-   Monitor with LangSmith.
-   Handle errors and logging.
-   Use a better vector database like Pinecone.

#### Example Dockerfile

``` dockerfile
FROM python:3.10-slim

WORKDIR /app

COPY . /app

RUN pip install -r requirements.txt

CMD ["streamlit", "run", "app.py", "--server.port=8501"]
```

> Take your project from a local prototype to a live, scalable
> application.

### 10. Key Takeaways

-   You learned how to build a complete LangChain project from scratch.
-   RAG helps your AI use private data.
-   Agents can take actions using tools.
-   This project can be extended with more tools, better UI and advanced
    workflows.

> "Build real projects. That's how you become job ready."

------------------------------------------------------------------------

# 100 LangChain Interview Questions

> The cover promised these — they were missing from the export, so here they are. Organized by section (2–20), five questions each, plus five foundational ones up front. Answers are short and interview-ready, not full essays; use the matching section above for the deeper explanation and code.

## Foundational (5)

1.  **Q: What problem does LangChain actually solve that calling an LLM API directly doesn't?**
    A: Raw API calls only get you text in, text out. LangChain standardizes prompting, chaining multi-step logic, connecting external data (RAG), giving models tools/actions, and keeping conversation state — so you're not rebuilding that plumbing for every project or every model provider.

2.  **Q: Is LangChain a model, a database, or an orchestration layer?**
    A: An orchestration layer. It doesn't train or host models, store vectors itself, or generate embeddings on its own — it provides a consistent interface to connect LLMs, vector stores, tools and data sources together.

3.  **Q: When would you *not* want to use LangChain?**
    A: For a single, simple prompt-in/response-out call with no chaining, retrieval, memory or tool use, a direct SDK call to the provider is simpler and has less overhead/abstraction to reason about.

4.  **Q: What's the difference between LangChain, LangGraph and LangSmith in one line each?**
    A: LangChain = components and chains for building LLM apps. LangGraph = stateful, graph-based orchestration for complex/looping agent workflows. LangSmith = tracing, evaluation and monitoring for those apps in dev and production.

5.  **Q: What is "LCEL" and why did LangChain move toward it?**
    A: LangChain Expression Language — composing components with the `|` operator (`prompt | model | parser`). It replaced many older `Chain` subclasses because it's more readable, supports streaming/async/batching uniformly, and composes better for branching and parallel execution.

## 2. LangChain Introduction + Why LangChain? (5)

6.  **Q: Name three prebuilt component categories LangChain provides.**
    A: Chains, agents, tools, memory, retrievers, output parsers — any three of these.

7.  **Q: Does using LangChain lock you into one LLM provider?**
    A: No — that's a core selling point. Swapping `ChatOpenAI` for `ChatAnthropic` or `ChatGoogleGenerativeAI` requires no change to the rest of the chain, since they share a common interface.

8.  **Q: What's LangChain Hub used for?**
    A: Sharing and pulling prebuilt, versioned prompts, chains and agents instead of writing them from scratch each time.

9.  **Q: Give a real-world example where LangChain is a poor architectural fit.**
    A: A latency-critical, single-turn classification endpoint with a fixed prompt and no retrieval/tools — the abstraction overhead adds little value there versus a direct API call.

10. **Q: What does "production-ready documentation and integrations" typically mean for a framework like this?**
    A: Battle-tested connectors (vector DBs, loaders, providers) with maintained versioning, plus first-party observability (LangSmith) rather than users hand-rolling logging/tracing themselves.

## 3. Installation + Project Setup (5)

11. **Q: Why should you use a virtual environment for a LangChain project?**
    A: To isolate project dependencies (LangChain, provider SDKs, vector store clients) from your global Python install and avoid version conflicts across projects.

12. **Q: Why split `langchain-openai`, `langchain-community` and `langchain-core` into separate packages instead of one big package?**
    A: To decouple release cadence and dependency weight — `langchain-core` holds stable base abstractions, `langchain-community` holds third-party integrations that change often, and provider packages (like `langchain-openai`) version independently of the core.

13. **Q: Why use a `.env` file instead of hardcoding an API key?**
    A: Prevents secrets from being committed to source control, allows different keys per environment (dev/staging/prod), and keeps credentials out of shared code.

14. **Q: What does `LANGCHAIN_TRACING_V2=true` do?**
    A: Enables automatic tracing of LangChain runs to LangSmith, so every LLM/chain/tool call in the app is recorded without extra code.

15. **Q: How do you verify a LangChain installation succeeded beyond just `pip install` finishing?**
    A: Import it and print `langchain.__version__`, or run a minimal script that makes a real LLM call end-to-end — pip succeeding doesn't guarantee the environment's API keys/config are correct.

## 4. Models + LLMs + Chat Models (5)

16. **Q: What's the practical difference between an LLM object and a Chat Model object in LangChain?**
    A: LLMs take a raw string and return a raw string completion (single-turn). Chat models take a list of role-tagged messages (system/human/AI) and return a message — built for multi-turn, instruction-following interactions.

17. **Q: What does `temperature` control, and what would you set it to for a data-extraction task?**
    A: Randomness/creativity of sampling. For deterministic, structured extraction you'd set it low, typically `0`.

18. **Q: What happens if you exceed a model's context window?**
    A: The call fails or the provider truncates/rejects the input — you need to chunk input (text splitters) or summarize/retrieve only relevant context instead of sending everything.

19. **Q: Why prefer streaming for a chat UI over waiting for the full response?**
    A: It reduces perceived latency — the user sees tokens appear immediately instead of staring at a blank screen until the entire generation finishes.

20. **Q: What's the benefit of LangChain's unified model interface when switching from GPT-4o to Claude or Gemini?**
    A: The surrounding chain (prompts, parsers, retrievers) doesn't need to change — only the model instantiation line does, since all chat models expose the same `.invoke()`/`.stream()` contract.

## 5. Prompts + Prompt Templates (5)

21. **Q: Why use a `PromptTemplate` instead of an f-string?**
    A: It validates that required input variables are provided, integrates directly into LCEL chains (`prompt | model`), and is portable/reusable across the app instead of scattered string formatting.

22. **Q: When would you choose few-shot prompting over zero-shot?**
    A: When the task's expected format or reasoning pattern is hard to describe in words alone but easy to demonstrate with 2-3 examples — e.g. a specific output structure or a niche classification scheme.

23. **Q: What's the risk of an overly long, unfocused prompt?**
    A: It burns context/tokens, can dilute the model's attention on the actually important instruction, and makes outputs less consistent run to run.

24. **Q: What does `ChatPromptTemplate.from_messages()` give you that a plain template doesn't?**
    A: The ability to define distinct system/user/assistant turns, which chat models are specifically trained to respect (system instructions get different weight than user text).

25. **Q: How would you constrain a prompt to force JSON-only output?**
    A: Explicit format instructions in the prompt (e.g. "respond with only valid JSON matching this schema") combined with a parser like `JsonOutputParser`/`PydanticOutputParser`, and ideally `OutputFixingParser` as a fallback.

## 6. Messages + Message History (5)

26. **Q: What are the three most common message roles, and what does each represent?**
    A: `SystemMessage` (sets behavior/instructions), `HumanMessage` (user input), `AIMessage` (model's own prior responses) — used together to represent a structured conversation.

27. **Q: Why pass a list of message objects instead of one big concatenated string?**
    A: The model was trained to distinguish roles; a flat string loses that structure and can make the model less reliably follow system instructions vs. user requests.

28. **Q: What is `ToolMessage` used for?**
    A: Representing the result returned by a tool call back to the model, so the model can incorporate that result into its next response.

29. **Q: What does `ChatMessageHistory` store, and where does that live by default?**
    A: An ordered list of message objects for a conversation; by default it's in-memory (lost on process restart) unless backed by persistent storage.

30. **Q: How would you give a chatbot memory that survives a server restart?**
    A: Back the message history with persistent storage (e.g. Redis, a database, or a vector store) instead of the default in-memory `ChatMessageHistory`.

## 7. Chains + LCEL (5)

31. **Q: What does the `|` operator actually do between two LCEL components?**
    A: Wires the output of the left component as the input to the right one, returning a new `Runnable` that can itself be invoked, streamed, or composed further.

32. **Q: How do you run two independent sub-chains in parallel with LCEL?**
    A: Use a dict literal of chains, e.g. `{"summary": chain1, "translation": chain2}` — LangChain's `RunnableParallel` (implicit from dict syntax) executes them concurrently.

33. **Q: What does `RunnablePassthrough` do and when is it needed?**
    A: Forwards its input unchanged. It's used in RAG-style chains so the original question reaches the final prompt alongside the retrieved context, e.g. `{"context": retriever, "question": RunnablePassthrough()}`.

34. **Q: What's `RunnableBranch` used for?**
    A: Conditional routing — picking which sub-chain to run based on a predicate function evaluated against the input, similar to an if/elif chain expressed declaratively.

35. **Q: Why is LCEL considered easier to debug than nested legacy `Chain` classes?**
    A: Each step is a separate, inspectable `Runnable`; you can invoke, stream or trace any individual piece in isolation, and LangSmith traces the whole pipe visually step by step.

## 8. Output Parsers + Structured Output (5)

36. **Q: Why is structured output important for production LLM applications?**
    A: Downstream code (APIs, databases, other services) needs a predictable shape to consume — free-form text can't be reliably parsed or validated without it.

37. **Q: What's the advantage of `PydanticOutputParser` over `JsonOutputParser`?**
    A: It parses into a typed, validated model (with field types, defaults, and validation logic) rather than a loosely-typed dict, catching malformed data early.

38. **Q: What does `OutputFixingParser` actually do under the hood?**
    A: When the base parser fails on malformed output, it sends the broken output back to an LLM with instructions to fix the formatting, then retries parsing.

39. **Q: What's a risk of relying entirely on `OutputFixingParser` instead of good prompting?**
    A: It costs an extra LLM call (latency + money) every time output is malformed, and it can mask a prompt-quality problem you should actually fix at the source.

40. **Q: How would you extract three named fields from a model's answer reliably?**
    A: Define a `ResponseSchema`/Pydantic model with those three fields, pass its format instructions into the prompt, and parse the response with the matching structured/Pydantic parser.

## 9. Embeddings + Vector Stores (5)

41. **Q: In one sentence, what does an embedding model do?**
    A: Converts text (or other data) into a fixed-length numerical vector such that semantically similar inputs produce vectors that are close together.

42. **Q: Why is cosine similarity typically preferred over Euclidean distance for text embeddings?**
    A: Cosine similarity measures the angle between vectors, which is more robust to differences in vector magnitude and better reflects semantic direction/meaning for text.

43. **Q: What's stored in a vector store besides the raw vector?**
    A: Metadata about the source chunk — e.g. document source, page number, chunk ID — used for filtering and for tracing an answer back to its origin.

44. **Q: Name two reasons you might choose Pinecone over a local FAISS index.**
    A: Managed, scalable infrastructure that doesn't require you to run/maintain the index yourself, and easier multi-node or cloud-native deployment versus an in-process/local index.

45. **Q: What happens to retrieval quality if you switch embedding models mid-project without re-embedding old documents?**
    A: It breaks — vectors from different embedding models live in incompatible spaces, so similarity search across a mixed set becomes meaningless. You must re-embed everything with the new model.

## 10. Document Loaders + Text Splitters (5)

46. **Q: What does a `Document` object contain?**
    A: `page_content` (the text) and `metadata` (a dict describing its source, e.g. filename, page number).

47. **Q: Why not just send an entire 50-page PDF as one chunk to the LLM?**
    A: It likely exceeds the context window, is expensive in tokens, and dilutes retrieval relevance — smaller, focused chunks retrieve and reason better.

48. **Q: What's the purpose of `chunk_overlap` in a text splitter?**
    A: Preserves some shared context between adjacent chunks so information split across a chunk boundary isn't lost entirely from either chunk's perspective.

49. **Q: Why is `RecursiveCharacterTextSplitter` the common default over a plain `CharacterTextSplitter`?**
    A: It tries a hierarchy of separators (paragraphs, then sentences, then words) so it respects natural text structure instead of cutting mid-sentence at a fixed character count.

50. **Q: If retrieval quality is poor, what's a first thing to check related to chunking?**
    A: Whether `chunk_size` is too large (diluting relevance) or too small (losing necessary context), and whether metadata needed for filtering is actually being preserved through the splitter.

## 11. Retrievers + RAG (5)

51. **Q: What does RAG add on top of a plain LLM call?**
    A: It retrieves relevant external documents based on the query and feeds them into the prompt as context, grounding the answer in real data instead of relying solely on the model's training knowledge.

52. **Q: Why does RAG reduce hallucination rather than eliminate it?**
    A: The model is now grounded in retrieved context, so it's less likely to invent facts, but it can still misinterpret or hallucinate on top of that context, or retrieval itself can surface irrelevant/wrong documents.

53. **Q: When would a BM25 (keyword) retriever outperform a vector retriever?**
    A: For queries relying on exact terms, codes, IDs or rare keywords where semantic similarity doesn't distinguish well — lexical match finds the exact string a vector search might blur past.

54. **Q: What problem does a Multi-Query Retriever solve?**
    A: A single phrasing of a query might miss relevant documents phrased differently; generating several reworded queries and merging results improves recall.

55. **Q: Name two ways to evaluate a RAG system beyond just reading outputs manually.**
    A: Retrieval metrics like Recall/Precision/MRR/Hit Rate for the retrieval step, and answer-quality metrics like groundedness/relevance/correctness for the generation step (e.g. via LangSmith evaluators).

## 12. Tools + Tool Calling (5)

56. **Q: What three things define a LangChain tool?**
    A: A name, a description (which the LLM reads to decide when/how to use it), and a function that executes and returns a result.

57. **Q: Why does the tool's description matter so much?**
    A: The LLM uses that description text — not the code — to decide whether and how to call the tool, so a vague or misleading description leads to wrong or missed tool usage.

58. **Q: What's the difference between direct tool calling (`bind_tools`) and using an agent?**
    A: Direct tool calling is for a known, single-step task where you decide when to call the tool. An agent decides at runtime, potentially across multiple steps, whether and which tools to call based on reasoning.

59. **Q: What's a security risk specific to tool-using LLM applications?**
    A: The model could be manipulated (via prompt injection) into calling a tool with harmful or unintended arguments — e.g. deleting data or hitting an unauthorized endpoint — if tool permissions aren't restricted.

60. **Q: How would you limit the blast radius of a tool that can run arbitrary code or queries?**
    A: Use an allowlist of permitted actions/tools, validate and sanitize arguments before execution, and apply least-privilege access (read-only DB credentials, sandboxed execution, etc.).

## 13. Agents + Agent Loops (5)

61. **Q: What differentiates an "agent" from a simple chain?**
    A: A chain follows a fixed sequence of steps. An agent decides at each step — using the LLM's own reasoning — what to do next, including whether to call a tool, and can loop until it determines the task is done.

62. **Q: Describe the ReAct loop in your own words.**
    A: Thought (reason about what to do) → Action (call a tool) → Observation (read the tool's result) → repeat until enough information is gathered → Final Answer.

63. **Q: What's a practical risk of letting an agent loop unconstrained?**
    A: It can loop indefinitely or take excessive tool calls (cost/latency), so production agents need a max-iteration limit or explicit stopping conditions.

64. **Q: When would you choose "Plan and Execute" over "Zero Shot ReAct"?**
    A: For longer, more complex multi-step tasks where committing to an upfront plan avoids the inefficiency/instability of purely reactive, step-by-step decision-making.

65. **Q: Why give an agent memory in addition to tools?**
    A: Without memory, the agent forgets earlier steps/results within a long task or across conversation turns, causing repeated tool calls or losing track of the original goal.

## 14. Memory + Conversation History (5)

66. **Q: Why can't you just keep appending every message forever to a `ConversationBufferMemory`?**
    A: Eventually the accumulated history exceeds the model's context window and increases token cost on every call — long conversations need windowing or summarization instead.

67. **Q: What trade-off does `ConversationSummaryMemory` make?**
    A: It compresses older messages into a summary to save tokens and stay within context limits, at the cost of losing some verbatim detail from earlier in the conversation.

68. **Q: What does `ConversationSummaryBufferMemory` try to balance?**
    A: Keeping recent messages verbatim (for accuracy on the immediate context) while summarizing older ones (for long-term efficiency) — a hybrid of buffer and summary approaches.

69. **Q: What is Entity Memory good for that plain buffer memory isn't?**
    A: Explicitly tracking specific facts (names, places, preferences) across a conversation so they can be recalled precisely even if the surrounding chat log is summarized or trimmed away.

70. **Q: How would you give a chatbot memory that persists across sessions for the same user?**
    A: Store the message history (or a vector-store-backed long-term memory) keyed by user ID in persistent storage — e.g. a database or `VectorStoreRetrieverMemory` — rather than relying on in-process memory.

## 15. Callbacks + Streaming (5)

71. **Q: What's the difference between a callback and streaming?**
    A: A callback is a hook that fires on specific execution events (start, new token, end, error) for logging/monitoring. Streaming specifically refers to receiving the response incrementally, token by token — often implemented using callback events under the hood.

72. **Q: Name three callback events besides `on_llm_new_token`.**
    A: Any three of: `on_llm_start`, `on_llm_end`, `on_chain_start`, `on_chain_end`, `on_tool_start`, `on_tool_end`, `on_error`.

73. **Q: Why avoid heavy processing inside a callback handler?**
    A: Callbacks fire synchronously during execution (e.g. per token); slow logic inside them adds latency to every single event and can noticeably slow the whole pipeline.

74. **Q: How does streaming improve perceived UX even if total generation time is unchanged?**
    A: The user sees output appearing immediately instead of a blank wait, which reduces perceived latency even though the wall-clock time to full completion is the same.

75. **Q: What's a production use for callbacks beyond just printing tokens?**
    A: Logging token usage/cost and latency per call, feeding structured logs to a monitoring system, or triggering alerts on `on_error`.

## 16. LangGraph Fundamentals (5)

76. **Q: What does LangGraph add that a simple LCEL chain can't do?**
    A: Persistent shared state across steps, explicit loops/cycles, conditional branching driven by that state, and human-in-the-loop pauses — LCEL chains are fundamentally linear/DAG-shaped, not cyclic.

77. **Q: What are the three core building blocks of a LangGraph graph?**
    A: Nodes (functions that read/update state), edges (define what runs next), and state (the shared data structure passed through the graph).

78. **Q: How does a conditional edge decide the next node?**
    A: A function inspects the current state and returns a key; that key is mapped to the actual next node name in the `add_conditional_edges` mapping.

79. **Q: Why would you want a loop back to a previous node in LangGraph?**
    A: For retry logic, iterative refinement, or multi-step reasoning where the agent needs to reattempt or continue working until some condition in the state is satisfied.

80. **Q: What's "human in the loop" used for in a LangGraph workflow?**
    A: Pausing execution at a node to get explicit human approval, correction or input before continuing — useful for sensitive or high-stakes actions.

## 17. Multi Agent Systems + Workflows (5)

81. **Q: What's the core motivation for using multiple agents instead of one big agent with many tools?**
    A: Splitting responsibility lets each agent specialize (clearer prompts, tighter tool sets, easier debugging) and can improve accuracy versus one agent trying to juggle every role and every tool at once.

82. **Q: Describe the "Supervisor" multi-agent architecture.**
    A: A central supervisor agent receives the task, decides which specialized sub-agent should handle each part, and coordinates their outputs into a final result — sub-agents don't need to know about each other.

83. **Q: What's a downside of adding more and more agents to a system?**
    A: Increased complexity in coordination, more places for errors/miscommunication to occur, higher latency/cost from multiple LLM calls, and harder debugging.

84. **Q: How do agents typically share information in a LangGraph-based multi-agent system?**
    A: Through the shared state object — each agent/node reads what it needs from state and writes its results back into it for the next agent to consume.

85. **Q: When is a "Sequential" architecture preferable to a "Collaborative" one?**
    A: When the task naturally decomposes into ordered, dependent stages (e.g. research → analyze → write) where each stage's output is a clean input to the next, rather than agents needing to negotiate or iterate together.

## 18. LangSmith + Tracing + Evaluation (5)

86. **Q: What's the core value proposition of LangSmith in one sentence?**
    A: Visibility into every step of an LLM application's execution (inputs, outputs, latency, cost) so you can debug, evaluate and improve it with real data instead of guessing.

87. **Q: What environment variables are needed for automatic tracing?**
    A: `LANGCHAIN_TRACING_V2=true`, `LANGCHAIN_API_KEY`, and typically `LANGCHAIN_PROJECT` to organize runs.

88. **Q: What's a "dataset" used for in LangSmith?**
    A: A collection of test examples (input + expected output) used to run repeatable evaluations/experiments so you can compare prompt, model or chain changes against a fixed benchmark.

89. **Q: Name two evaluation metrics LangSmith supports besides correctness.**
    A: Any two of: relevance, helpfulness, coherence, groundedness, or a custom-defined metric.

90. **Q: Why trace agent runs specifically, not just single LLM calls?**
    A: Agents involve multiple LLM calls and tool invocations per task; tracing the full sequence is the only way to pinpoint which specific step caused a wrong or slow outcome.

## 19. Security + Guardrails + Production (5)

91. **Q: What is prompt injection?**
    A: An attack where malicious input tries to override or ignore the system's original instructions, manipulating the model into producing unintended behavior or output.

92. **Q: Why prefer an allowlist over a blocklist for tool permissions?**
    A: A blocklist only blocks known bad cases and misses novel ones; an allowlist explicitly defines the safe subset of allowed actions, which is far harder to bypass.

93. **Q: Name three things audit logging should capture in a production LLM app.**
    A: Any three of: user inputs, model outputs, tool calls and their arguments, timestamps, token usage/cost, and errors.

94. **Q: What's the purpose of output content moderation separate from input validation?**
    A: Input validation only checks what the user sends; the model can still generate unsafe or policy-violating content on its own, so output must be checked independently before it reaches the user.

95. **Q: What compliance concern is most relevant when an LLM app processes user PII?**
    A: Data privacy regulations (e.g. GDPR, DPDP) — requiring data minimization, anonymization/redaction, and transparency about how user data is processed and stored.

## 20. End to End LangChain RAG + Agent Project (5)

96. **Q: In the example project's architecture, what's the role of the retriever versus the agent?**
    A: The retriever supplies grounded, relevant document context (knowledge); the agent decides what actions to take — including whether to use the retriever, web search, or other tools — to answer the user (action).

97. **Q: Why use `return_source_documents=True` in the `RetrievalQA` chain?**
    A: So the app can show users which source chunks the answer was grounded in — critical for trust, debugging retrieval quality, and citing sources in the UI.

98. **Q: Why containerize the app with Docker before deployment?**
    A: Ensures a consistent runtime environment (Python version, dependencies) between local development and production, avoiding "works on my machine" issues.

99. **Q: What's the argument for swapping Chroma for Pinecone when moving from prototype to production?**
    A: Pinecone is a managed, horizontally scalable vector database, better suited to production traffic and larger datasets than a local/embedded store like Chroma.

100. **Q: Beyond adding more tools, what are two ways to make this end-to-end project meaningfully more production-ready?**
    A: Any two of: add LangSmith tracing/evaluation, add input/output guardrails, add authentication, add proper error handling and logging, or move to a managed vector database with monitoring.

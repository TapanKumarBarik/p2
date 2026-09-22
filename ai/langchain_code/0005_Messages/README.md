# Basic usage

system_msg = SystemMessage("You are a helpful assistant.")
human_msg = HumanMessage("Hello, how are you?")


# Text prompts

Text prompts are strings - ideal for straightforward generation tasks where you don’t need to retain conversation history.

# Message prompts

```
from langchain.messages import SystemMessage, HumanMessage, AIMessage

messages = [
    SystemMessage("You are a poetry expert"),
    HumanMessage("Write a haiku about spring"),
    AIMessage("Cherry blossoms bloom...")
]
response = model.invoke(messages)


```
# System message


# Human message

# Text content

# AI message

When models make tool calls, they’re included in the AIMessage:


# Streaming and chunks


# Multimodal


# Serialization

You can serialize messages to plain objects for storage and deserialize back to message instances. This is useful for persisting conversation history and resuming sessions.
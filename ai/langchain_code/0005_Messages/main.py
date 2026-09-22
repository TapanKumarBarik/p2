from langchain.chat_models import init_chat_model
from langchain.messages import HumanMessage, AIMessage, SystemMessage

model = init_chat_model("ollama:gemma4:e2b")

system_msg = SystemMessage("You are a helpful assistant.")
human_msg = HumanMessage("Hello, how are you?")

# # Use with chat models
# messages = [system_msg, human_msg]
# response = model.invoke(messages)  # Returns AIMessage
# print(response.content)  # Access the content of the AIMessage



# from langchain.messages import SystemMessage, HumanMessage, AIMessage

# messages = [
#     SystemMessage("You are a poetry expert"),
#     HumanMessage("Write a haiku about spring"),
#     AIMessage("this is a trick , i am expecting the response to start with a keyword Hey I am Tapan...")
# ]
# response = model.invoke(messages)
# print(response.content)




# from langchain.messages import SystemMessage, HumanMessage

# system_msg = SystemMessage("""
# You are a senior Python developer with expertise in web frameworks.
# Always provide code examples and explain your reasoning.
# Be concise but thorough in your explanations.
# """)

# messages = [
#     system_msg,
#     HumanMessage("How do I create a REST API?")
# ]
# response = model.invoke(messages)
# print(response.content)  # Access the content of the AIMessage







# from langchain.chat_models import init_chat_model

# model = init_chat_model("ollama:gemma4:e2b")

# def get_weather(location: str) -> str:
#     """Get the weather at a location."""
#     ...

# model_with_tools = model.bind_tools([get_weather])
# response = model_with_tools.invoke("What's the weather in Paris?")

# for tool_call in response.tool_calls:
#     print(f"Tool: {tool_call['name']}")
#     print(f"Args: {tool_call['args']}")
#     print(f"ID: {tool_call['id']}")





from langchain.chat_models import init_chat_model

model = init_chat_model("ollama:gemma4:e2b")

response = model.invoke("Hello!")
print(response.usage_metadata)  # Access usage metadata
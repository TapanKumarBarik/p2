



"""
Agents

An agent is a model calling tools in a loop until a given task is complete.


Core components

"""

from langchain.tools import tool
from langchain.agents import create_agent ,AgentState

from pydantic import BaseModel


@tool
def search(query: str) -> str:
    """Search for information."""
    return f"Results for: {query}"

class Answer(BaseModel):
    summary: str
    confidence: float
    
    
    
class MyState(AgentState):
    user_id: str
    call_count: int

agent = create_agent(
    model="ollama:gemma4:e2b",
    tools=[search],
    system_prompt="You are a helpful assistant. Be concise and accurate.",
    response_format=Answer,
    state_schema=MyState,
    )


result = agent.invoke({"messages": [{"role": "user", "content": "Summarize AI trends"}]})
print(result)
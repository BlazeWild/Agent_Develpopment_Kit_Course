from google.adk.agents import Agent
from google.adk.tools import google_search, built_in_code_execution
from datetime import datetime

now = datetime.now()

def get_current_time()-> dict: #specify the return type as dict 
    """
    Get the current time in a dictionary format.
    """
    return {
        "current_time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "timezone": "UTC",
    }

# root_agent = Agent(
#     name = "tool_agent",
#     model="gemini-2.0-flash",
#     description="Tool agent",
#     instruction="""
#     You are a helpful assistant. That uses the following tools:
#     - google_search
#     """,
#     tools=[google_search],
#     # tools=[get_current_time],
# )

root_agent = Agent(
    name = "tool_agent",
    model="gemini-2.0-flash",
    description="Tool agent",
    instruction="""
    You are a helpful assistant. That uses the following tools:
    - code_execution
    """,
    tools=[built_in_code_execution],
    # tools=[get_current_time],
)

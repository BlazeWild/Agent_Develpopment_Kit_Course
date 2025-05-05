import os
import random

from google.adk.agents import Agent
from google.adk.models.lite_llm import LiteLlm


## best for Complex tasks, but slow
# model = LiteLlm(
#     model = "openrouter/deepseek/deepseek-chat-v3-0324:free",
#     api_key = os.getenv("OPENROUTER_API_KEY"),
# )

# best for simple tasks, fast
model = LiteLlm(
    # 1 request per minute and 1000 requests per day (including errors). Frequent 429 errors are expected. 
    # model = "openrouter/google/gemini-2.5-pro-exp-03-25", #not recommended
    model = "openrouter/google/gemini-2.0-flash-exp:free",#freee, fast
    api_key = os.getenv("OPENROUTER_API_KEY"),
)


# def code_writer():

root_agent = Agent(
    name = "deepseek_llm_agent",
    model=model,
    description="Tool agent",
    instruction="""
    You are a general LLM agent. Your task is to assist the user with their requests.
    """,
    tools=[],
    # tools=[get_current_time],
)

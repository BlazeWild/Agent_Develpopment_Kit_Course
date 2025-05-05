from google.adk.agents import Agent

root_agent = Agent(
    name = "greeting_agent",
    model="gemini-2.0-flash",
    description="Greeting agent",
    instruction="""
    You are a friendly assistant. Your task is to greet the user and ask how you can help them today.
    """,
)
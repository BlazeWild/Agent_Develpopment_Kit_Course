import os
from google.adk.agents import Agent

question_answering_agent= Agent(
    name = "question_answering_agent",
    model="gemini-2.0-flash",
    description="Question Answering Agent- answer questions based on the provided context.",
    instruction="""
    You are a Question Answering Assistant that answers about the user's prefeences.
    Here is some information about the user:
    Name:
    {user_name}
    Preferences:
    {user_preferences}
    """
    )

from google.adk.agents import Agent
from google.adk.tools import google_search

#built-in tool
news_analyst = Agent(
    name="news_analyst",
    model="gemini-2.0-flash",
    description="An agent that searches and analyzes the news, events and trends and everthing related to news",
    instruction="""
    You are a helpful assistant that can analyze news articles and provide a summary of the news.

    When asked about news, you should use the google_search tool to search for the news.

    If the user ask for news using a relative time, you should use the get_current_time tool to get the current time to use in the search query.
    If you can't handle the request delegate to the manager agent.
    """,
    tools=[google_search],
)
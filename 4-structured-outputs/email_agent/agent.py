import os
from google.adk.agents import Agent
from google.adk.models.lite_llm import LiteLlm
from pydantic import BaseModel, Field


class EmailContent(BaseModel):
    subject: str = Field(
        ...,description="The subject line of the email. Should be concise and descriptive"
        )
    body: str = Field(
        ...,description="The main content of the email. Shoul be well-formatted with proper greeing, paragraphs and closing"
        )

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
    name = "email_agent",
    model="gemini-2.0-flash",
    instruction="""
    You are an Email Generation Assistant.
    Your task is to generate a professional email based on the user's request.
    
    GUIDELINES:
    - create an appropriate subject line for the email.
    - Write a well-structured email bosy with:
        * Professional greeting
        * Clear and concise paragraphs
        * Appropriate closing statement
        * Youur name as signature
    - Suggest relevant attachments if applicable(empty list if not)
    - Email tone should match the purpose (e.g., formal, friendly, etc.)
    - Keep mail consise and to the point.
    
    IMPORTANT:
    - Your response MUST be a **valid raw JSON object**, with no Markdown, code blocks, or extra text.
    - Do NOT include any explanations, triple backticks (```), or formatting outside of the JSON object.
    - Return exactly this format:

    {
    "subject": "Subject line of the email here",
    "body": "Body of the email here with proper formatting and paragraphs"
    }
    """,
    description="Email Generation Assistant- generate a professional email based on the user's request.",
    output_schema=EmailContent,
    output_key="email",
    )

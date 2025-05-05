from google.adk.runners import Runner
from google.adk.sessions import DatabaseSessionService
from memory_agent.agent import memory_agent
from utils import call_agent_async
from dotenv import load_dotenv
import asyncio
import os
# from google.adk.sessions.sql_session_service import SQLSessionService

load_dotenv()

#===PART 1: Initialize persisitent Session Service===
#Using SQLite as the database for persistent storage
db_url = "sqlite:///./my_agent_data.db"
session_service = DatabaseSessionService(db_url=db_url)

# ==== PART 2: Define initial state ====
# this will only be used when creating a new session
initial_state={
    "user_name":"Ashok",
    "reminders":[],
}

async def main_async():
    #setup constants
    APP_NAME = "Memory Agent"
    USER_ID = "ashokaiagent"
     
    # ===PART 3: Sesion Management - Find or Create===
    # Check for existing sessions for this user
    existing_sessions = session_service.list_sessions(
        app_name= APP_NAME,
        user_id = USER_ID,
    )
    
    # If there's an existing session, use it, otherwise create a new one
    if existing_sessions and len(existing_sessions.sessions)>0:
        #Use the most recent session
        SESSION_ID = existing_sessions.sessions[0].id
        print(f"Using existing session ID: {SESSION_ID}")
    else:
        #Create a new session with the initial state
        new_session = session_service.create_session(
            app_name = APP_NAME,
            user_id = USER_ID,
            state = initial_state,
        )
        
        SESSION_ID = new_session.id
        print(f"Created new session:{SESSION_ID}")
        
    # ===PART 4: Agent Runner Setup ====
    # create a runner with the memory agent
    runner = Runner(
        agent=memory_agent,
        app_name=APP_NAME,
        session_service=session_service,
    )
        
    # === PART 5: Interactive Conversation Loop ====
    print("\nWelcome to the Memory Agent!")
    print("Your reminders will be remembered across conversations")
    print("Type 'exit' or quit to end the conversation. \n")
    print("Type 'exit' or 'quit' to end the conversation.\n")
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["exit", "quit"]:
            print("Ending conversation.Your data will be saved.")
            break
        
        #process the user query through the agent
        await call_agent_async(runner, USER_ID, SESSION_ID, user_input)


if __name__ == "__main__":
    asyncio.run(main_async())
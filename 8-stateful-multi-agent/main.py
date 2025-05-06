#for creating session, handling queries, and managing history

import asyncio
import os

#import the main customer service agent
from customer_service_agent.agent import customer_service_agent
from dotenv import load_dotenv, find_dotenv
from google.adk.runners import Runner
from google.adk.sessions import InMemorySessionService
from utils import add_user_query_to_history, call_agent_async

load_dotenv()   
print(f"GOOGLE_API_KEY: {os.getenv('GOOGLE_API_KEY')}")

#===PART 1: Initialize in-memory Session Service===
#Using in-mempry storage for this example(non-persistent)
session_service = InMemorySessionService()

#===PART 2: Define the initial state===
#this will be used when creating a new session
iniitial_state = {
    "user_name": "Blaze Wild",
    "purchased_courses":[],
    "interaction_history":[],
}

async def main_async():
    #Set up constants
    APP_NAME = "Customer Service Agent"
    USER_ID = "blazewild"
    
    #===PART 3: Create a session===
    #Create a session with the initial state
    new_session = session_service.create_session(
        app_name=APP_NAME,
        user_id=USER_ID,
        state=iniitial_state,
    )
    SESSION_ID = new_session.id
    print(f"Created new session with ID: {SESSION_ID}")
    
    
    #===PART 4: Agent runner Setup ===
    #Create a runner with the main customer service agent
    runner = Runner(
        agent = customer_service_agent,
        app_name = APP_NAME,
        session_service = session_service,
        
    )
    
    #===PART 5: Interactive Conversation Loop===
    print("Welcome to the Customer Service Agent!")
    print("Type 'exit' or 'quit' to end the conversation.\n")
    
    while True:
        #Get user input
        user_input = input("You: ")
        
        #Check for exit command
        if user_input.lower() in ["exit", "quit"]:
            print("Ending conversation. Goodbye!")
            break
        
        #Add user query to history
        add_user_query_to_history(
            session_service,APP_NAME, USER_ID, SESSION_ID, user_input
        )
        
        #Call the agent asynchronously and get the response
        await call_agent_async(runner, USER_ID, SESSION_ID, user_input)
    # === PART 6: State Examination ===
    #show final session state
    final_session = session_service.get_session(
        app_name = APP_NAME,user_id=USER_ID,session_id=SESSION_ID
    )
    print("\nFinal session state:")
    for key, value in final_session.state.items():
        print(f"{key}: {value}")

def main():
    """Entry point for the application"""
    #Run the main async function
    asyncio.run(main_async())
    
if __name__ == "__main__":
    main()
from dotenv import load_dotenv
from google.adk.runners import Runner
from google.adk.sessions import InMemorySessionService
from google.genai import types
from question_answering_agent.agent import question_answering_agent
import uuid

load_dotenv()

# Create new session service to store state
session_service_stateful = InMemorySessionService()

initial_state = {
    "user_name": "Ashok",
    "user_preferences": """
    I like to play football, basketball, and tennis
    My favourite food is Mexican.
    My favourite movie is Interstellar.
    Loves it when people call me Godfather.
    I am interested in learning about AI and ML.
    """,
}

# CREATE A NEW SESSION
APP_NAME = "Ashok"
USER_ID = "ashok"
SESSION_ID = str(uuid.uuid4())
stateful_session = session_service_stateful.create_session(
    app_name=APP_NAME,
    user_id=USER_ID,
    session_id=SESSION_ID,
    state=initial_state,
)

# Verify the session was created by retrieving it
verification_session = session_service_stateful.get_session(
    app_name=APP_NAME,
    user_id=USER_ID,
    session_id=SESSION_ID,
)

print("Session created with ID:", SESSION_ID)
print("Session created successfully:", verification_session is not None)
print("Session state matches:", verification_session.state == initial_state)
# print("Session object attributes:", dir(stateful_session))

runner = Runner(
    agent=question_answering_agent,
    app_name=APP_NAME,
    session_service=session_service_stateful,
)

new_message = types.Content(
    role="user",
    parts=[types.Part(text="What do i like?")],
)

for event in runner.run(
    user_id=USER_ID,
    session_id=SESSION_ID,
    new_message=new_message,
):
    if event.is_final_response():
        if event.content and event.content.parts:
            print(f"Final response: {event.content.parts[0].text}")
            
    print("-------SESSION EVENT EXPLORATION-------")
    session = session_service_stateful.get_session(
        app_name=APP_NAME,
        user_id=USER_ID,
        session_id=SESSION_ID,
    )
    print(f"Session ID: {SESSION_ID}")
    print(f"Session state: {session.state}")
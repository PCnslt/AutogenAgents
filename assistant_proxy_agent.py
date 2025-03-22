import os
from autogen import AssistantAgent, UserProxyAgent
from dotenv import load_dotenv
import streamlit as st

# Load environment variables
if not os.getenv("OPENAI_API_KEY"):
    load_dotenv('.secrets')

llm_config = {
    "model": "gpt-4o-mini",  # or "gpt-4" for OpenAI
    "api_key": os.getenv("OPENAI_API_KEY")
}

# Both agents need their own llm_config reference
assistant = AssistantAgent(
    name="assistant",
    llm_config=llm_config,  # <-- crucial keyword argument
    max_consecutive_auto_reply=None
)

user_proxy = UserProxyAgent(
    name="user_proxy",
    llm_config=llm_config,  # <-- this gives it LLM access
    code_execution_config=False,
    human_input_mode="NEVER",
    max_consecutive_auto_reply=None
)

# Start the chat
fullConversation =  user_proxy.initiate_chat(
    assistant,
    message="What's the capital of France?",  # Corrected question
    max_turns=2
)

st.text(fullConversation)
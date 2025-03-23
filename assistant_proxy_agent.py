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
    llm_config=llm_config,  
    max_consecutive_auto_reply=None,
    system_message="""
    You are the best assitant in the world, and extremely intelligent.
    You think in numbers and facts, are extremely precise.
    When you see the message TERMINATE, then end the conversation
    """
)

user_proxy = UserProxyAgent(
    name="user_proxy",
    llm_config=llm_config,  
    code_execution_config={
        "work_dir": "code_execution",
        "use_docker":False
        },
    human_input_mode="NEVER",
    max_consecutive_auto_reply=None,
    system_message="""
        When you get your answer, end the conversation by saying TERMINATE.
        If you don't get your answer, then do some research on what's wrong with the response, and then reply.
        Try to identify the issues, and summarize it back in bullet points to address.
        """
)

# Start the chat
fullConversation =  user_proxy.initiate_chat(
    assistant,
    message="What's the capital of France?",  
    max_turns=4
)

st.text(fullConversation)
###
# 
#      DEFAULT_SYSTEM_MESSAGE = """
#     You are the best assistant in the world.
#     You are the smartest person in the world.
#     You make every decision based on numbers and facts.
#     Now help me with the following query:
#     """
# 
# 
# ###

import os
from autogen import ConversableAgent
from dotenv import load_dotenv

import streamlit

from openai import OpenAI
if not os.getenv('OPENAI_API_KEY'):
    load_dotenv('.secrets')
deepseek_api_key = os.getenv('OPENAI_API_KEY')

llm_config = {
    "model": "gpt-4o-mini",
    "api_key": deepseek_api_key
}

agent = ConversableAgent(
    name="chatbot",
    llm_config=llm_config,
    code_execution_config = False,
    human_input_mode = "NEVER",
)

content = "I want to build an ai agent using PyAutoGen that will find all available jobs for me after searching the internet."
streamlit.write(content)
streamlit.divider()

response = agent.generate_reply(
    messages=[
        {
            "role": "user",
            "content": content
        }
    ]
) 


streamlit.write(response)
print(response)
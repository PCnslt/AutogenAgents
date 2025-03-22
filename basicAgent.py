import os
from autogen import ConversableAgent
from dotenv import load_dotenv


if not os.getenv('DEEPSEEK_API_KEY')
    load_dotenv('.secrets')
deepseek_api_key = os.getenv('DEEPSEEK_API_KEY')

llm_config = {
    "model": "gpt-4o-mini",
    "api_key": deepseek_api_key
}
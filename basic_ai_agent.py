###
# This class initializes an AI chatbot with a specified 
# language model and allows users to interact with it via 
# a web interface.
# 
# app = AIAgentApp()
#
# # Call the method you want to use, e.g., generate_response
# user_input = "Tell me what's the best business idea to solve with ai agent?"
# response = app.generate_response(user_input)  # Use the method to generate a response
#
# # Print or use the generated response as needed
# print(response)
#
# 
# 
# ###
import os
import streamlit as st
from autogen import ConversableAgent
from dotenv import load_dotenv

class AIAgentApp:
    def __init__(self):
        # Load API Key
        if not os.getenv('OPENAI_API_KEY'):
            load_dotenv('.secrets')
        self.openai_api_key = os.getenv('OPENAI_API_KEY')

        # LLM Configuration
        self.llm_config = {
            "model": "gpt-4o-mini",
            "api_key": self.openai_api_key
        }

        # Initialize Agent
        self.agent = ConversableAgent(
            name="chatbot",
            llm_config=self.llm_config,
            code_execution_config=False,
            human_input_mode="NEVER",
        )

    def run(self):
        # Streamlit UI
        st.title("AI Job Search Agent")
        st.write("Enter your query and press 'Search' to find jobs using PyAutoGen.")

        user_input = st.text_area("Enter your query:")

        if st.button("Search"):
            if user_input.strip():  # Ensure input is not empty
                st.write("Searching... Please wait.")

                # Generate Response
                response = self.generate_response(user_input)

                # Display response
                st.subheader("AI Response:")
                st.write(response)  # Directly write response

                # Print in console
                print(response)
            else:
                st.warning("Please enter a query before searching.")

    def generate_response(self, user_input):
        return self.agent.generate_reply(
            messages=[
                {
                    "role": "user",
                    "content": user_input
                }
            ]
        )

# Entry point of the application
if __name__ == "__main__":
    app = AIAgentApp()
    app.run()

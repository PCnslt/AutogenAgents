import os
from autogen import AssistantAgent, UserProxyAgent
from autogen.code_utils import create_virtual_env
from autogen.coding import CodeBlock, LocalCommandLineCodeExecutor
from dotenv import load_dotenv
import streamlit as st
from autogen.code_utils import create_virtual_env



# First skill: Get stock prices
def get_stock_prices(stock_symbols, start_date, end_date):
    """Get the stock prices for the given stock symbols between
    the start and end dates.

    Args:
        stock_symbols (str or list): The stock symbols to get the
        prices for.
        start_date (str): The start date in the format 
        'YYYY-MM-DD'.
        end_date (str): The end date in the format 'YYYY-MM-DD'.
    
    Returns:
        pandas.DataFrame: The stock prices for the given stock
        symbols indexed by date, with one column per stock 
        symbol.
    """
    import yfinance

    stock_data = yfinance.download(
        stock_symbols, start=start_date, end=end_date
    )
    return stock_data.get("Close")

# Second skill: Plot stock prices
def plot_stock_prices(stock_prices, filename):
    """Plot the stock prices for the given stock symbols.

    Args:
        stock_prices (pandas.DataFrame): The stock prices for the 
        given stock symbols.
    """
    import matplotlib.pyplot as plt

    plt.figure(figsize=(10, 5))
    for column in stock_prices.columns:
        plt.plot(
            stock_prices.index, stock_prices[column], label=column
                )
    plt.title("Stock Prices")
    plt.xlabel("Date")
    plt.ylabel("Price")
    plt.grid(True)
    plt.legend()
    plt.savefig(filename)

# Load environment variables
if not os.getenv("OPENAI_API_KEY"):
    load_dotenv('.secrets')
    
deepseek_coder_config = {
    "config_list": [
        {
            "model": "deepseek-coder-v2-lite-instruct-mlx",
            "price": [999.0, 999.0],
            "base_url": "http://192.168.1.170:1234/v1",
            "api_key": "deepseek-coder-v2-lite-instruct-mlx",
        }
    ],
    "timeout": 120  
}
meta_config = {
    "config_list": [
        {
            "model": "meta-llama-3.1-8b-instruct",
            "price": [999.0, 999.0],
            "base_url": "http://192.168.1.170:1234/v1",
            "api_key": "meta-llama-3.1-8b-instruct",
        }
    ],
    "timeout": 120  
}


llm_config = {
    "config_list":[
        {
    "model": "gpt-3.5-turbo",  # or "gpt-4" for OpenAI
    "api_key": os.getenv("OPENAI_API_KEY")}],
    "timeout": 120
}

assistant = AssistantAgent(
    name="assistant",
    llm_config=deepseek_coder_config,  
    code_execution_config=False,
    max_consecutive_auto_reply=None,
    system_message="""
    You are the worlds best Programming engineer at MIT Labs.
    You know everything about Computer Science, IT and Computer Engineering.
    You just got hired as a Python Developer.
    You're objective is to write Python code that is: 
        * efficient
        * modular
        * reusable
        * proper logging
        * error handling 
        * bug free.
    Whenever needed create python code to search the internet, and scrape the internet.
    Create your own python environment to do eerything.
    You always remember the original context of the conversation. So that when you recieve any feedback, you do:
        * make sure you update the parts that needed to be updated.
        * if that doesn't fix your problem in last 2 tries, then may be rethink your whole approach.
    """
)

venv_dir = ".env_llm"
venv_context = create_virtual_env(venv_dir)

executor = LocalCommandLineCodeExecutor(
    virtual_env_context=venv_context,
    timeout=200,
    work_dir="coding",
    functions=[get_stock_prices, plot_stock_prices],
)
print(
    executor.execute_code_blocks(code_blocks=[
        CodeBlock(
            language="python", 
            code="import sys; print(sys.executable)"
            )
        ])
)

user_proxy = UserProxyAgent(
    name="user_proxy",
    # llm_config=deepseek_coder_config,
    code_execution_config={
        ""
        "executor": executor},
    human_input_mode="NEVER", ## <====
    max_consecutive_auto_reply=None,
    system_message="""
        You are the supervisor to your new intern from MIT's PhD Department.
        If you don't get your answer, then do some research on what's wrong with the response, and then reply.
        Try to identify the issues, and summarize it back in bullet points to address.
        If you don't have the solution, then ask assistant to fix it.
        Ensure original task in context/question is accomplished.
        After 2 to 3 failed attempts, send TERMINATE command.
        When you see the following messages then end the conversation:
            - exitcode: 0 (execution succeeded)
            - TERMINATE
            - please don't hesitate to ask. (or something similar)
        """
)

user_proxy.initiate_chat(
    assistant,
    max_turns=10,
    # message="""
    # Plot a chart of META and TSLA stock price changes.
    # """
    message= "Create a plot showing the normalized price of NVDA and BTC-USD for the last 5 years. "\
"Also plot the 60 weeks moving average normalized price for each asset. "\
"Make sure the code is in markdown code block, print the normalized prices, save the figure"\
" to a file asset_analysis.png and who it. Provide all the code necessary in a single python bloc. "\
"Re-provide the code block that needs to be executed with each of your messages. "\
"If python packages are necessary to execute the code, provide a markdown "\
"sh block with only the command necessary to install them and no comments."
)
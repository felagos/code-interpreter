from dotenv import load_dotenv
from langchain import hub
from langchain_openai import ChatOpenAI
from langchain.agents import create_react_agent, AgentExecutor
from langchain_experimental.tools import PythonREPLTool

if __name__ == '__main__':
    load_dotenv()

    print("Start...")

    instructions = """You are an agent designed to write and execute python code to answer questions.
       You have access to a python REPL, which you can use to execute python code.
       If you get an error, debug your code and try again.
       Only use the output of your code to answer the question. 
       You might know the answer without running any code, but you should still run the code to get the answer.
       If it does not seem like you can write code to answer the question, just return "I don't know" as the answer.
    """

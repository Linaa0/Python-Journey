
from langchain_core.messages import HumanMessage
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.tools import tool
from langchain.agents import create_agent
from dotenv import load_dotenv

load_dotenv()

@tool 
def calculator(a:float,b:float)-> str:
    """Useful for performing basic arithmetic calculations with numbers"""
    print("Tool has been called")
    return f"The sum of {a} and {b} is {a+b}"

def say_Hello(name:str)-> str:
    """Useful for greeting people"""
    print("Tool has been called")
    return f"Hello, {name}"

def main():
     model = ChatGoogleGenerativeAI(model="gemini-3.5-flash", temperature=0)

     tools= [calculator, say_Hello]
     agent_executor= create_agent(model, tools)

     print("Welcome! I am your AI assistant, Type 'quit' to exist.")
     print("You can ask me to perform calculations or chat with me.")

     while True:
        user_input=input("\nYou: ").strip()

        if user_input=='quit':
            break

        print("\n Assistant: ", end="")

        response= agent_executor.invoke(
            {"messages": [HumanMessage(content=user_input)]}
        )
        latest_message= response["messages"][-1]

        if isinstance(latest_message.content, list):
            for item in latest_message.content:
                # Look at the active loop item, not an index row!
                if isinstance(item, dict) and "text" in item:
                    print(item["text"], end="")
            print() # Print a final clean newline when done
            
        else:
            # Fallback if it returns a standard text string
            print(latest_message.content)
        # print(latest_message.content, end="")
                # for message in chunk["agent"]["messages"]:
                #       print(message.content, end="")

        print()

if __name__== "__main__":
     main()        


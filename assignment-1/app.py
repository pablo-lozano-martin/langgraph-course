from langgraph.graph import START, END, MessagesState, StateGraph
from langchain_core.messages import HumanMessage, AIMessage, SystemMessage
from langchain_openai import ChatOpenAI
import os
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '../.env')
load_dotenv(dotenv_path)

OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")

graph = StateGraph(MessagesState)

llm = ChatOpenAI(model="gpt-4.1-mini", temperature=0, api_key=OPENAI_API_KEY)

def assistant(state: MessagesState) -> MessagesState:
    return {
        "messages": llm.invoke(state["messages"])
    }

graph.add_node("assistant", assistant)

graph.add_edge(START, "assistant")
graph.add_edge("assistant", END)

app = graph.compile()

messages = [HumanMessage(content="Hello, can you help me with my assignment?")]

response = app.invoke({"messages": messages})

for m in response["messages"].content:
    print("----"*20)
    print(m)
from langgraph.graph import START, END, MessagesState, StateGraph
from langchain_core.messages import HumanMessage, AIMessage, SystemMessage
from langchain_openai import ChatOpenAI
from langgraph.prebuilt import ToolNode, tools_condition
from langchain_community.tools import DuckDuckGoSearchRun
from langgraph.checkpoint.memory import MemorySaver

import os
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '../.env')
load_dotenv(dotenv_path)

OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")

duckduckgo_search = DuckDuckGoSearchRun()
tools = [duckduckgo_search]

graph = StateGraph(MessagesState)

llm = ChatOpenAI(model="gpt-4.1-mini", temperature=0, api_key=OPENAI_API_KEY)


llm_with_tools = llm.bind_tools(tools, parallel_tool_calls=False)

def assistant(state: MessagesState) -> MessagesState:
    return {
        "messages": llm_with_tools.invoke(state["messages"])
    }

graph.add_node("assistant", assistant)
graph.add_node("tools", ToolNode(tools))

graph.add_edge(START, "assistant")
graph.add_conditional_edges("assistant", tools_condition)
graph.add_edge("tools", "assistant")

memory = MemorySaver()

config = { "configurable": {"thread_id": "1"} }

app = graph.compile(checkpointer = memory)

messages = [HumanMessage(content="what about Sevilla?")]

messages = app.invoke({"messages": messages}, config)

for m in messages["messages"]:
    print("----"*20)
    print(m)
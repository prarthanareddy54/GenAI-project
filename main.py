import os

import streamlit as st
from dotenv import load_dotenv
from langchain_core.messages import AIMessage, HumanMessage
from langchain_core.tools import tool
from langchain_groq import ChatGroq
from langgraph.prebuilt import create_react_agent

load_dotenv()

DEFAULT_MODEL = "qwen/qwen3.6-27b"


@tool
def calculator(a: float, b: float) -> str:
    """Add two numbers."""
    return f"The sum of {a} and {b} is {a + b}"


@tool
def say_hello(name: str) -> str:
    """Greet a person by name."""
    return f"Hello {name}, I hope you are well today"


def create_agent(model_name: str):
    model = ChatGroq(model=model_name, temperature=0)
    return create_react_agent(model, [calculator, say_hello])


st.set_page_config(page_title="PythonAIChatbot", page_icon="✦")
st.title("✦ PythonAIChatbot")
st.caption("A simple Groq chat assistant with calculator and greeting tools.")

with st.sidebar:
    st.header("Settings")
    model_name = st.text_input(
        "Groq model",
        value=os.getenv("GROQ_MODEL", DEFAULT_MODEL),
        help="qwen/qwen3.6-27b is the configured free-tier model.",
    )
    if st.button("New chat", use_container_width=True):
        st.session_state.messages = []
        st.rerun()

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("Ask something..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        response_placeholder = st.empty()
        response = ""
        history = [
            HumanMessage(content=item["content"])
            if item["role"] == "user"
            else AIMessage(content=item["content"])
            for item in st.session_state.messages
        ]
        try:
            agent = create_agent(model_name)
            for chunk, _metadata in agent.stream(
                {"messages": history}, stream_mode="messages"
            ):
                if isinstance(chunk.content, str):
                    response += chunk.content
                    response_placeholder.markdown(response + "▌")
            response_placeholder.markdown(response or "I could not generate a response.")
        except Exception as error:
            response = f"Unable to connect to Groq. Check your API key and model.\n\n`{error}`"
            response_placeholder.error(response)

    st.session_state.messages.append({"role": "assistant", "content": response})

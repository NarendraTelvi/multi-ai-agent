import streamlit as st
from langchain_groq import ChatGroq

llm = ChatGroq(
    model="qwen/qwen3.8-27b",
    temperature=0,
    groq_api_key=st.secrets["GROQ_API_KEY"]
)
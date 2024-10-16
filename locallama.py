from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_community.llms import Ollama

import streamlit as st
import os
from dotenv import load_dotenv

load_dotenv()
##langsmith tracking
os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_API_KEY"] = os.getenv('LANGSMITH_API')



##prompt template
prompt=ChatPromptTemplate.from_messages(
    [
        ("system","you are heplful assistant. please respones to the userv quries"),
        ("user","Question:{question}")
    ]
)

##streamlit framework
st.title("Langchain Demo with LLAMA2 API")
input_text = st.text_input("Search the topic u want")

#ollama LLAma2 LLM
llm=Ollama(model='llama2')
output_parser=StrOutputParser()
chain=prompt|llm|output_parser

if input_text:
    st.write(chain.invoke({'question':input_text}))
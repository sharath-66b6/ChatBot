from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

import streamlit as st
import os
from dotenv import load_dotenv

load_dotenv()
os.environ['GROQ_API_KEY'] = os.getenv('GROQ_API', "not found")
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
st.title("Langchain Demo with OPENAI API")
input_text = st.text_input("Search the topic u want")

#openAI LLM
llm=ChatGroq(model='mixtral-8x7b-32768')
output_parser=StrOutputParser()
chain=prompt|llm|output_parser

if input_text:
    st.write(chain.invoke({'question':input_text}))
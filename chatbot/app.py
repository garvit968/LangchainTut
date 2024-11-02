from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

import streamlit as st
from dotenv import load_dotenv
import os

load_dotenv()
os.environ['OPENAI_API_KEY'] = os.getenv('OPENAI_API_KEY')
os.environ['LANGCHAIN_TRACING_V2'] = os.getenv('LANGCHAIN_TRACING_V2')
os.environ['LANGCHAIN_API_KEY'] = os.getenv('LANGCHAIN_API_KEY')

## PROMPT TEMPLATE

prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a helpful> Please response"),
        ("user","Question:{question}")
    ]
)

## Streamlit
st.title('Langchain demo')
input_text = st.text_input("Type text to search")

## oPen AI LLM
llm = ChatOpenAI(model = 'gpt-3.5-turbo')
output_parser = StrOutputParser()
chain = prompt|llm|output_parser

if input_text:
    st.write(chain.invoke({'question': input_text}))
import requests
import streamlit as st

def get_openai_response(input_text):
    response = requests.post('http://localhost:8000/essay/invoke',
                             json={'input': {'topic':input_text}})
    
    return response.json()['output']['content']

def get_ollama_response(input_text2):
    response = requests.post('http://localhost:8000/poem/invoke',
                             json={'input': {'topic':input_text2}})
    
    return response.json()['output']['content']

st.title('Welcome to chatbit')
input_text = st.text_input("write essaty on")
input_text2 = st.text_input("Write poem")

if input_text:
    st.write(get_openai_response(input_text))
if input_text2:
    st.write(get_ollama_response(input_text2))
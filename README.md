# Multi-Model Application: RAG, Similarity Search, and Q&A


This project integrates multiple natural language processing (NLP) models and tools to create a unified application that leverages the power of retrieval-augmented generation (RAG), similarity search, and question-answering. The application utilizes state-of-the-art models from OpenAI, Hugging Face, Ollama, and community-driven libraries to deliver advanced NLP capabilities.

## Table of Content
- Key Features
- Prerequisites
- Installation 
- File Structure


## Key Features

### 1. RAG Application (OpenAI)

- Implements a Retrieval-Augmented Generation (RAG) framework using OpenAI's language models to answer user queries by retrieving relevant information from a corpus and generating responses.  

### 2. Similarity Search (Ollama)

- Vectorizes documents locally and online using Ollama, a tool for document embedding, enabling efficient similarity-based search.

### 3. Question-Answering (Hugging Face)

- Uses Hugging Face's Msitral model to build a Q&A system where users can ask questions, and the model retrieves and generates accurate answers from the provided corpus.

### 4. Unified Workflow with LangChain

- All the above features are integrated and orchestrated using LangChain, a powerful framework that allows for easy chaining of models and tools.
Community-provided PromptTemplates for streamlined prompt management and dynamic responses.
### 5. Vector Stores

- Chroma and FAISS are used as vector stores to enable fast and efficient semantic search across large document corpora.

## Prerequisites
- pypdf
- langchain
- streamlit
- faiss-cpu
- langchain_openai 
- langchain_core
- python-dotenv
- langchain_community
- langserve
- fastapi
- uvicorn
- bs4
- chromadb
- langchainhub
- sentence_transformers

## Installation

1. Install Dependencies 
```bash
pip install -r requirements.txt
```

2. Make sure to setup following API keys:
```bash
OPENAI_API_KEY=your_openai_api_key
HF_TOKEN=your_hugging_face_token
OLLAMA_API_KEY=your_ollama_api_key
```
3. Install FAISS: FAISS may need to be installed separately depending on your system. Follow the installation instructions from the `FAISS GitHub page`.

## Folder Structure
```bash
.
├── api/
│   ├── app.py               # Main application logic
│   └── client.py            # Streamlit application logic
├── chatbot/
│   ├── app.py               # Main application logic
│   └── locallama.py         # Ollama local logic 
├── HuggingFace/
│   ├── us_census/           # Data files 
│   └── huggingface.ipynb    # HuggingFace application logic
├── rag/
│   ├── attention.pdf        # Document file to Search
│   ├── simplerag.ipynb      # RAG application logic
│   └── speech.txt           # Speech Info to Search
├── requirements.txt         # Python dependencies
├── .env                     # Environment variables (API keys, tokens)
└── README.md                # Project documentation

```
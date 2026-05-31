import json
import os

from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma
from langchain_groq import ChatGroq
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationalRetrievalChain

# Load API Key
with open("config.json", "r", encoding="utf-8") as f:
    config = json.load(f)

GROQ_API_KEY = config["GROQ_API_KEY"]


def setup_vectorstore():
    embeddings = HuggingFaceEmbeddings()

    vectorstore = Chroma(
        persist_directory="vector_db_dir",
        embedding_function=embeddings
    )

    return vectorstore


def create_chain():

    vectorstore = setup_vectorstore()

    llm = ChatGroq(
        groq_api_key=GROQ_API_KEY,
        model="llama-3.3-70b-versatile",
        temperature=0
    )

    retriever = vectorstore.as_retriever(
        search_kwargs={"k": 3}
    )

    memory = ConversationBufferMemory(
        memory_key="chat_history",
        return_messages=True,
        output_key="answer"
    )

    chain = ConversationalRetrievalChain.from_llm(
        llm=llm,
        retriever=retriever,
        memory=memory,
        return_source_documents=True,
        verbose=False
    )

    return chain
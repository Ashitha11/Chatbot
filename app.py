#creating a chatbot
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser       #You can also make custom output parser

import streamlit as st
import os
from dotenv import load_dotenv

os.environ['OPENAI_API_KEY']='<OPENAI_API_KEY'

##for Langsmith tracking
#os.environ['LANGCHAIN_TRACING_V2']="true"
#os.environ['LANGCHAIN_API_KEY']=os.getenv('LANCHAIN_API_KEY')

##Prompt template

prompt = ChatPromptTemplate.from_messages(
    [
        ("system","You are a helpful assistant. Please respond to user queries."),      #response from AI
        ("user","Question:{question}")                                                  #ques by user
    ]
)

##streamlit

st.title('Langchain Demo with OpenAI')
input_text=st.text_input("Search the topic you want")

##openAI LLM

llm = ChatOpenAI(model="gpt-3.5-turbo")
output_parser = StrOutputParser()
chain = prompt|llm|output_parser

if input_text:
    st.write(chain.invoke({'question':input_text}))
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint

import streamlit as st

from dotenv import load_dotenv
load_dotenv()


llm = HuggingFaceEndpoint(
    repo_id="deepseek-ai/DeepSeek-R1-0528",
    task="text-generation",
    max_new_tokens=200,
    do_sample=False,
    repetition_penalty=1.03,
    provider="auto"
)

chat_model = ChatHuggingFace(llm=llm)

st.header("Research Tool")

user_input = st.text_input("Enter your prompt")

if st.button('Summarize'):
    result = chat_model.invoke(user_input)
    st.write(result.content)
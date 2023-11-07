import langchain_helper as lch
import streamlit as st

#to run --> python3 -m streamlit run main.py                                            

st.title("Trevs Personal Assistant")

language = st.sidebar.selectbox("Language",("English","Spanish","German","French"))

if language == "English":
    freeform_text = st.sidebar.text_area(label="What is your question?",
    max_chars=100)

if language == "Spanish":
    freeform_text = st.sidebar.text_area(label="What is your question?",
    max_chars=100)

if language == "German":
    freeform_text = st.sidebar.text_area(label="What is your question?",
    max_chars=100)

if language == "French":
    freeform_text = st.sidebar.text_area(label="What is your question?",
    max_chars=100)

if freeform_text:
    response = lch.my_chatbot(language,freeform_text)
    st.text(response['text'])
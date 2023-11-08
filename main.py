import langchain_helper as lch
import streamlit as st

# to launch streamlit app
# python3 -m streamlit run main.py                                            

st.title("Trevs Personal Assistant")

language = st.sidebar.selectbox("Language",("English","Spanish","German","French"))

if language != None:
    freeform_text = st.sidebar.text_area(label="What is your question?",
    max_chars=100)

if freeform_text:
    response = lch.my_chatbot(language,freeform_text)
    st.text(response['text'])

import google.generativeai as genai
import streamlit as st
api_key="Your api key here"
genai.configure(api_key=api_key)
model=genai.GenerativeModel("gemini-2.5-flash")
st.header("Welcome to the Gemini chatbot")
text=st.chat_input("How can i help you today or write exit")

if text:
    if text == "exit":
        st.write("Okay goodbye")
        st.stop()
    response=model.generate_content(text)
    st.write(response.text)
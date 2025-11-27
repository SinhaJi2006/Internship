import streamlit as st

with st.chat_message("user","ASSISTANT","AI","HUMAN"):
  st.audio("path/to/audio/file.mp3")
  st.camera_input("Take a picture")
  st.text_input("Enter your name :")
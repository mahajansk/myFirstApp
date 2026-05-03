import streamlit as st
st.title("My First Web App")
name = st.text_input("What is Your Name")
if name:
    st.success(f"Hello, {name}! Your app is live")

import streamlit as st

st.title("Resume")

content = """Please find my resume attached below for your review and consideration. You may download it by clicking 
on the provided link."""

st.info(content)

st.image("images/Young_Jun_Lee_RESUME.png")

with open("images/Young_Jun_Lee_RESUME.png", "rb") as file:
    btn = st.download_button(
            label="Download image",
            data=file,
            file_name="Young_Jun_Lee_RESUME.png",
            mime="imageS/Young_Jun_Lee_RESUME.png"
          )
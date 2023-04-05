import streamlit as st

st.set_page_config(layout="wide")

column_1, column_2 = st.columns(2)

with column_1:
    st.image("images/photos.png", width= 500)

with column_2:
    st.title("Young Lee")
    content = """I'm currently a George Mason University student graduating Fall 2023. I major in Information Technology
     with a concentration in  cyber security. I've built this web app to showcase myself and my knowledge in 
     programming. I have a great desire to learn new concepts and technologies to further my career and knowledge. 
     On my free time I enjoy reading comics, discovering new music, and spending time with friends. Some of my hobbies 
     are working out, playing basketball, and programming.  
    """
    st.info(content)
st.write("**Below you can find some of my personal projects I've created. Feel free to contact me!**")
import streamlit as st
import pandas

st.set_page_config(layout="wide")

column_1, empty_column, column_2 = st.columns([1.5, 0.5, 1.5])

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

column_3, column_4 = st.columns(2)

data_file = pandas.read_csv('data.csv', sep=";")

with column_3:
    for index, row in data_file[:10].iterrows():
        st.header(row['title'])
        st.write(row['description'])
        st.image("images/" + row['image'])
        st.write(f"[Source Code]({row['url']})")

with column_4:
    for index, row in data_file[10:].iterrows():
        st.header(row['title'])
        st.write(row['description'])
        st.image("images/" + row['image'])
        st.write(f"[Source Code]({row['url']})")

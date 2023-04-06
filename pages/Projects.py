import streamlit as st
import pandas

st.title("Projects")
content = "Personal project I have created to showcase my knowledge in programming."
st.info(content)

column_3, column_4 = st.columns(2)

data_file = pandas.read_csv('pages/data.csv', sep=";")

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

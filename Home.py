import streamlit as st

st.set_page_config(layout="wide")

column_1, empty_column, column_2 = st.columns([1.5, 0.5, 1.5])

with column_1:
    st.image("images/photos.png", width= 500)

with column_2:
    st.title("Young Lee")
    content = """Hi there! My name is Young Lee, and I am a student at George Mason University with a passion for 
    programming. I have honed my skills in python, html, CSS, and more. I am driven by my love for to always learn new 
    skills and my desire to apply my skills to solve real world problems. I am always eager to take on new challenges 
    and expand my skill set, and I thrive in collaborative environments where I can work with other talented 
    professionals. When I'm not working, you can find me working out, reading comics, or playing team sports. My desire
    to learn inspires me to think creatively and approach challenges from new angles. I believe that these experiences 
    and interests help me to bring a unique perspective to my work and allow me to create truly innovative solutions for
    my employers. Thank you for taking the time to visit my portfolio website! Please feel free to browse my work and 
    get in touch if you have any questions.  
    """
    st.info(content)



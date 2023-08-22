import streamlit as st


st.title('Welcome to python dashboard')
st.header('header')
image = st.file_uploader('upload a file')
if image:
    st.image(image)


    st.write('hello')
#


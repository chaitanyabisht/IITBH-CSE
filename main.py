import streamlit as st
st.title('Welcome to course website for IIT Bhilai')
st.subheader('Browse courses below')

option = st.selectbox(
     'Select the course',
     ('CS200 - Software Tools and Technologies II', 'CS254 - Database and Management Systems', 'CS250 - Operating Systems'))

st.write('You selected:', option)


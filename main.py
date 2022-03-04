import streamlit as st
import api


st.title('Welcome to course website for IIT Bhilai')
st.subheader('Browse courses below')

browse = False

if (not browse):
    course = st.selectbox(
     'Select the course', api.course_list())
else:
    st.write('hello')


if st.button('Browse'):
    browse = True
    


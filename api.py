import requests as r
import streamlit as st

@st.cache
def course_list():
    lst = r.get('https://api.github.com/orgs/IIT-Bhilai-CSE/repos?type=all').json()
    return [item['name'] for item in lst]


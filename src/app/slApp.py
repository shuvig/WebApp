import sys
import os

parent_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(parent_dir)

import streamlit as st

from src.app.htmlTemplate import css

st.set_page_config(
    page_title="Chat with multiple PDFs",
    page_icon=":books:",
    layout="wide",
    initial_sidebar_state="expanded",
)
st.write(css, unsafe_allow_html=True)
st.header("Chat with multiple PDFs :books:")
user_question = st.text_input("Ask a question")

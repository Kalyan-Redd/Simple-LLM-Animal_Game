# Entry point: defines the two pages and the navigation between them.
import streamlit as st

st.set_page_config(page_title="Animal Guessing Game", page_icon="🐾")

pages = [
    st.Page("play.py", title="Play"),
    st.Page("stats.py", title="Stats"),
]
st.navigation(pages).run()

import streamlit as st
from app_pages.page_summary import page_summary

st.set_page_config(
    page_title="FloodSave",
    page_icon="🌊",
    layout="wide"
)

page_summary()

# app.py
# Entry point for the FloodSave Streamlit dashboard
# Handles page configuration, CSS loading and sidebar navigation
# Criteria: 5.4 (Streamlit dashboard), 6.3 (navigation menu)

import streamlit as st
from src.styles import apply_custom_css
from app_pages.page_summary import page_summary
from app_pages.page_flood_risk_study import page_flood_risk_study
from app_pages.page_hypothesis_validation import page_hypothesis_validation
from app_pages.page_risk_predictor import page_risk_predictor
from app_pages.page_model_performance import page_model_performance

# page configuration — must be first Streamlit call
st.set_page_config(
    page_title="FloodSave",
    page_icon="🌊",
    layout="wide"
)

# load shared CSS once — all pages inherit styles from src/styles.py
apply_custom_css()

# sidebar navigation — criteria 6.3
with st.sidebar:
    st.markdown('<div class="fs-title">FloodSave</div>', unsafe_allow_html=True)
    st.markdown(
        '<div class="fs-subtitle">Irish Flood Risk Prediction</div>',
        unsafe_allow_html=True
    )
    page = st.radio(
        "Navigation",
        options=[
            "Project Summary",
            "Flood Risk Study",
            "Hypothesis Validation",
            "Risk Predictor",
            "Model Performance"
        ],
        label_visibility="hidden"
    )

# route to selected page
if page == "Project Summary":
    page_summary()
elif page == "Flood Risk Study":
    page_flood_risk_study()
elif page == "Hypothesis Validation":
    page_hypothesis_validation()
elif page == "Risk Predictor":
    page_risk_predictor()
elif page == "Model Performance":
    page_model_performance()
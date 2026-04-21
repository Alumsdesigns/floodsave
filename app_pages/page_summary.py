# Purpose: Project summary page — overview, dataset, business requirements
# Criteria: 1.1, 6.1

import streamlit as st
from src.styles import metric_card, section_header, info_box


def page_summary():
    st.markdown('<div class="fs-title">FloodSave</div>', unsafe_allow_html=True)
    st.markdown('<div class="fs-subtitle">Irish Flood Risk Prediction System</div>', unsafe_allow_html=True)

    section_header("Project Overview")
    info_box("FloodSave predicts flood risk and flood depth for Irish locations using real OPW hydrometric station data. Built for construction companies, insurers, local councils and the public.")

    section_header("Dataset at a Glance")

    col1, col2, col3, col4 = st.columns(4)
    with col1:
        metric_card("Stations", "457", "OPW monitoring stations")
    with col2:
        metric_card("Features", "12", "Engineered columns")
    with col3:
        metric_card("Risk Classes", "3", "High, Medium, Low")
    with col4:
        metric_card("Data Source", "Live", "waterlevel.ie API")

    section_header("Business Requirements")

    col1, col2, col3 = st.columns(3)
    with col1:
        metric_card("BR1", "Understand Risk", "Which features correlate with flood risk")
    with col2:
        metric_card("BR2", "Classify Risk", "Predict High / Medium / Low for any location")
    with col3:
        metric_card("BR3", "Predict Depth", "Estimate flood depth in metres")

    section_header("Target Users")

    col1, col2 = st.columns(2)
    with col1:
        info_box("Construction — Site risk assessment before breaking ground")
        info_box("Insurance — Property flood risk premium pricing")
    with col2:
        info_box("Local Government — Emergency planning and infrastructure")
        info_box("Public — Personal safety decisions during heavy rainfall")

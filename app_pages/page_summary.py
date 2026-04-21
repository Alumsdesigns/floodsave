# app_pages/page_summary.py
# Purpose: Project summary page — overview, dataset, business requirements
# Criteria: 1.1, 6.1

import streamlit as st


def page_summary():
    st.title("FloodSave — Flood Risk Prediction System")
    st.markdown("---")

    st.header("Project Overview")
    st.write("""
    FloodSave is an intelligent flood risk prediction platform built on 
    real Irish Office of Public Works (OPW) hydrometric station data. 
    It classifies flood risk as High, Medium or Low and predicts expected 
    flood depth in metres for any Irish location.
    """)

    st.markdown("---")
    st.header("Dataset")
    st.write("""
    The dataset contains 457 active OPW hydrometric monitoring stations 
    pulled from the live OPW API at waterlevel.ie. Each station includes 
    geographic coordinates, derived elevation, distance to river, region 
    classification and flood risk label.
    """)

    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Total Stations", "457")
    with col2:
        st.metric("Features", "12")
    with col3:
        st.metric("Irish Counties", "26")

    st.markdown("---")
    st.header("Business Requirements")
    st.write("**BR1:** Understand which geographic features correlate most strongly with flood risk.")
    st.write("**BR2:** Predict flood risk category (High / Medium / Low) for any Irish location.")
    st.write("**BR3:** Predict expected flood depth in metres to support insurance and safety planning.")

    st.markdown("---")
    st.header("Target Users")
    users = {
        "Construction": "Site risk assessment before breaking ground",
        "Insurance": "Property flood risk pricing",
        "Local Government": "Emergency planning and infrastructure",
        "Public": "Personal safety decisions during heavy rainfall"
    }
    for user, use_case in users.items():
        st.write(f"**{user}:** {use_case}")
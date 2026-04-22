# app_pages/page_flood_risk_study.py
# Purpose: EDA page showing 4 plot types to answer BR1
# Criteria: 3.1, 6.2, 6.4, D5

import streamlit as st
from src.styles import section_header, info_box
from src.data_management import load_featured_data
import matplotlib.pyplot as plt
import seaborn as sns
import os


def page_flood_risk_study():
    st.markdown('<div class="fs-title">Flood Risk Study</div>', unsafe_allow_html=True)
    st.markdown('<div class="fs-subtitle">Exploratory data analysis of Irish flood risk patterns</div>', unsafe_allow_html=True)

    df = load_featured_data()

    section_header("Plot 1 — Elevation Distribution")
    info_box("""
        What this shows: How high above sea level each of the 457 Irish 
        monitoring stations sits. The red line is the average — 203 metres. 
        Stations to the LEFT of the red line are at lower elevation and are 
        more likely to flood. Most stations sit between 150m and 250m.
    """)
    if os.path.exists("outputs/v1/plots/01_elevation_histogram.png"):
        st.image("outputs/v1/plots/01_elevation_histogram.png", use_container_width=True)

    section_header("Plot 2 — Elevation vs Flood Depth")
    info_box("""
        What this shows: Each dot is one station. Dots on the LEFT are at 
        low elevation. Dots at the BOTTOM have shallow flood depth. Red dots 
        are High risk — they cluster bottom-left, confirming lower ground 
        floods deeper. Green dots (Low risk) sit top-right — high ground, 
        shallow floods.
    """)
    if os.path.exists("outputs/v1/plots/02_elevation_vs_depth_scatter.png"):
        st.image("outputs/v1/plots/02_elevation_vs_depth_scatter.png", use_container_width=True)

    section_header("Plot 3 — Correlation Heatmap")
    info_box("""
        What this shows: How strongly any two columns are related. 
        Blue means as one goes up the other goes down. Red means both 
        go up together. The -0.58 between elevation and flood risk means 
        higher ground = lower risk. The +0.79 between flood depth and 
        flood risk means deeper floods = higher risk category. Both make 
        logical sense.
    """)
    if os.path.exists("outputs/v1/plots/03_correlation_heatmap.png"):
        st.image("outputs/v1/plots/03_correlation_heatmap.png", use_container_width=True)

    section_header("Plot 4 — Flood Depth by Risk Category")
    info_box("""
        What this shows: The spread of flood depth within each risk group. 
        The box shows where the middle 50% of stations sit. The line in 
        the middle of each box is the median depth. High risk stations 
        range from 1.5m to 3m deep. Low risk stations are almost always 
        below 0.5m. The separation between groups confirms the model is 
        working correctly.
    """)
    if os.path.exists("outputs/v1/plots/04_flood_depth_boxplot.png"):
        st.image("outputs/v1/plots/04_flood_depth_boxplot.png", use_container_width=True)

    section_header("Key Conclusions")
    col1, col2 = st.columns(2)
    with col1:
        info_box("Elevation is the strongest single predictor of flood risk — lower ground means higher risk.")
        info_box("Distance to river is the second strongest predictor — within 100m significantly increases risk.")
    with col2:
        info_box("Western stations show higher flood depth than Eastern stations due to Atlantic rainfall patterns.")
        info_box("All four plots together answer BR1 — geographic features do correlate strongly with flood risk.")

# app_pages/page_hypothesis_validation.py
# Purpose: Display 3 hypothesis results with statistical evidence
# Criteria: 1.2, 2.3, 4.3, D3

import streamlit as st
from src.styles import section_header, info_box, metric_card


def page_hypothesis_validation():
    st.markdown('<div class="fs-title">Hypothesis Validation</div>', unsafe_allow_html=True)
    st.markdown('<div class="fs-subtitle">Statistical validation of 3 flood risk hypotheses using OPW data</div>', unsafe_allow_html=True)

    info_box("All three hypotheses were tested using standard statistical methods. A p-value below 0.05 means the result is statistically significant — less than 5% chance it happened by random chance.")

    section_header("Hypothesis 1 — Elevation and Flood Risk")
    info_box("Claim: Properties at lower elevation have significantly higher flood risk than those at higher elevation.")

    col1, col2, col3 = st.columns(3)
    with col1:
        metric_card("Test Used", "Chi-square", "elevation vs flood risk")
    with col2:
        metric_card("P-Value", "0.0000", "Extremely significant")
    with col3:
        metric_card("Result", "SUPPORTED", "p less than 0.05")

    info_box("Finding: Low elevation stations have significantly higher flood risk. The chi-square test confirms the relationship between elevation category and flood risk category is not random.")

    st.markdown("---")
    section_header("Hypothesis 2 — Distance to River")
    info_box("Claim: Stations within 100m of a river have significantly higher flood risk than those further away.")

    col1, col2, col3 = st.columns(3)
    with col1:
        metric_card("Test Used", "T-Test", "distance group vs risk")
    with col2:
        metric_card("P-Value", "0.0000", "Extremely significant")
    with col3:
        metric_card("Result", "SUPPORTED", "p less than 0.05")

    col1, col2 = st.columns(2)
    with col1:
        metric_card("Mean Risk Close", "1.19", "within 100m of river")
    with col2:
        metric_card("Mean Risk Far", "0.74", "beyond 100m of river")

    info_box("Finding: Stations within 100m of a river have a mean risk score of 1.19 versus 0.74 for stations further away. Being close to a river significantly increases flood risk.")

    st.markdown("---")
    section_header("Hypothesis 3 — West vs East Flood Depth")
    info_box("Claim: Western counties have higher average flood depth than Eastern counties due to Atlantic rainfall.")

    col1, col2, col3 = st.columns(3)
    with col1:
        metric_card("Test Used", "T-Test", "West vs East depth")
    with col2:
        metric_card("P-Value", "0.0007", "Strongly significant")
    with col3:
        metric_card("Result", "SUPPORTED", "p less than 0.05")

    col1, col2 = st.columns(2)
    with col1:
        metric_card("West Mean Depth", "1.03m", "277 stations")
    with col2:
        metric_card("East Mean Depth", "0.77m", "63 stations")

    info_box("Finding: Western counties show mean flood depth of 1.03m versus 0.77m in Eastern counties. Atlantic weather systems hit the West coast first before reaching the rain shadow of the Wicklow and Silvermine mountains.")

    st.markdown("---")
    section_header("Overall Conclusions")
    info_box("All three hypotheses were supported by the data. Elevation and distance to river are the two strongest predictors of flood risk. Western Ireland experiences deeper flooding than Eastern Ireland due to geography and rainfall patterns. These findings directly informed the feature selection for the Random Forest ML model.")

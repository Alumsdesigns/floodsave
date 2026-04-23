# app_pages/page_risk_predictor.py
# Purpose: User inputs location attributes and gets flood risk prediction
# Criteria: 4.1, 5.4, D7

import streamlit as st
import folium
from streamlit_folium import st_folium
from src.styles import section_header, info_box, metric_card, risk_badge, result_box
from src.ml_pipeline import predict_flood_risk


def page_risk_predictor():
    st.markdown('<div class="fs-title">Flood Risk Predictor</div>',
                unsafe_allow_html=True)
    st.markdown('<div class="fs-subtitle">Adjust the sliders to match your location then click Predict</div>',
                unsafe_allow_html=True)

    info_box("Use the sliders to set your location details. The model predicts flood risk based on 457 OPW monitoring stations across Ireland.")

    section_header("Location Inputs")

    col1, col2 = st.columns(2)
    with col1:
        elevation = st.slider(
        "Elevation (metres)",
        min_value=0, max_value=300,
        value=150, step=5,
        help="Sea level is 0m. Highest point in Ireland (Carrauntoohil) is 1039m but most habitable land is under 300m"
        )
        distance = st.slider(
        "Distance to nearest river (metres)",
        min_value=0, max_value=500,
        value=200, step=10,
        help="0m means on the riverbank. 500m is the maximum distance in the dataset"
        )
    with col2:
        latitude = st.slider(
        "Latitude — Cork 51.9, Dublin 53.3, Donegal 54.7",
        min_value=51.4, max_value=55.4,
        value=53.3, step=0.1,
        help="Move north to south across Ireland"
        )
        longitude = st.slider(
        "Longitude — Galway -9.0, Dublin -6.3",
        min_value=-10.5, max_value=-5.4,
        value=-7.8, step=0.1,
        help="Move west to east across Ireland"
        )

    region = "West" if longitude < -8.0 else "East" if longitude > -7.0 else "Midlands"
    st.write(f"Region: {region}")

    # initialise session state
    if 'prediction_result' not in st.session_state:
        st.session_state.prediction_result = None
        st.session_state.prediction_inputs = None

    if st.button("Predict Flood Risk", type="primary"):
        result = predict_flood_risk({
            'elevation_m': elevation,
            'distance_to_river_m': distance,
            'latitude': latitude,
            'longitude': longitude
        })
        st.session_state.prediction_result = result
        st.session_state.prediction_inputs = {
            'latitude': latitude,
            'longitude': longitude,
            'region': region
        }

    # show results if prediction has been run
    if st.session_state.prediction_result is not None:
        result = st.session_state.prediction_result
        inputs = st.session_state.prediction_inputs
        risk = result['risk_category']
        depth = result['flood_depth_m']

        st.markdown("---")
        section_header("Prediction Results")

        col1, col2, col3 = st.columns(3)
        with col1:
            metric_card("Risk Category", risk, "Predicted classification")
        with col2:
            metric_card("Flood Depth", f"{depth}m", "Predicted depth")
        with col3:
            metric_card("Region", inputs['region'], "Based on longitude")

        st.markdown("<br>", unsafe_allow_html=True)
        risk_badge(risk)
        st.markdown("<br>", unsafe_allow_html=True)

        if risk == "High":
            result_box("<strong>High flood risk.</strong> Low elevation and close to a river. Flood mitigation measures are strongly recommended.")
        elif risk == "Medium":
            result_box("<strong>Medium flood risk.</strong> Moderate risk level. Standard flood precautions are advised.")
        else:
            result_box("<strong>Low flood risk.</strong> Favourable elevation and distance from water. Flood risk is minimal.")

        section_header("Location Map")
        colour_map = {"High": "red", "Medium": "orange", "Low": "green"}
        m = folium.Map(
            location=[inputs['latitude'], inputs['longitude']],
            zoom_start=10
        )
        folium.Marker(
            location=[inputs['latitude'], inputs['longitude']],
            popup=f"{risk} Risk — {depth}m predicted depth",
            tooltip=f"Click for details",
            icon=folium.Icon(color=colour_map[risk], icon="info-sign")
        ).add_to(m)
        st_folium(m, width=700, height=400)

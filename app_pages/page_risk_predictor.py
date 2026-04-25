# Purpose: User inputs location by name or clicks map to get flood risk prediction
# Criteria: 4.1, 5.4, D7

import streamlit as st
import folium
from streamlit_folium import st_folium
from geopy.geocoders import Nominatim
from geopy.exc import GeocoderTimedOut
from src.styles import section_header, info_box, metric_card, result_box
from src.ml_pipeline import predict_flood_risk
from src.data_management import get_location_name

IRELAND_BOUNDS = {
    'lat_min': 51.4, 'lat_max': 55.4,
    'lon_min': -10.5, 'lon_max': -5.4
}

def geocode_location(location_name):
    try:
        geolocator = Nominatim(user_agent="FloodSave/1.0")
        location = geolocator.geocode(f"{location_name}, Ireland", timeout=5)
        if location:
            lat = location.latitude
            lon = location.longitude
            if (IRELAND_BOUNDS['lat_min'] <= lat <= IRELAND_BOUNDS['lat_max'] and
                    IRELAND_BOUNDS['lon_min'] <= lon <= IRELAND_BOUNDS['lon_max']):
                return lat, lon
        return None, None
    except GeocoderTimedOut:
        return None, None

def get_region(longitude):
    if longitude < -8.0:
        return "West"
    elif longitude > -7.0:
        return "East"
    return "Midlands"

def run_prediction(elevation, distance, lat, lon):
    return predict_flood_risk({
        'elevation_m': elevation,
        'distance_to_river_m': distance,
        'latitude': lat,
        'longitude': lon
    })

def page_risk_predictor():
    COLOUR_MAP = {"High": "red", "Medium": "orange", "Low": "green"}  # defined once, used in two places below
    st.markdown('<div class="fs-title">Flood Risk Predictor</div>',
                unsafe_allow_html=True) 
    st.markdown('<div class="fs-subtitle">Search any Irish location or click the map to get a flood risk prediction</div>',
                unsafe_allow_html=True)

    # initialise session state
    if 'pred_result' not in st.session_state:
        st.session_state.pred_result = None
        st.session_state.pred_lat = 53.3
        st.session_state.pred_lon = -7.8
        st.session_state.pred_location = "Ireland"
        st.session_state.pred_region = "Midlands"

    # two column layout — inputs left, map right
    col_left, col_right = st.columns([1, 1])

    with col_left:
        section_header("Search Location")
        info_box("Type any Irish town, city or area. The model predicts flood risk based on 457 OPW monitoring stations Or click anywhere on the map to predict flood risk for that location.")

        location_input = st.text_input(
            "Town, city or area",
            placeholder="e.g. Athlone, Galway, Cork, Dublin..."
        )

        if location_input:
            lat, lon = geocode_location(location_input)
            if lat and lon:
                st.session_state.pred_lat = lat
                st.session_state.pred_lon = lon
                st.session_state.pred_location = location_input
                st.session_state.pred_region = get_region(lon)
                info_box(f"Found: {get_location_name(lat, lon)}")
            else:
                st.warning("Location not found in Ireland. Try a different name.")

        section_header("Fine-tune")
        elevation = st.slider(
            "Elevation (metres)",
            min_value=0, max_value=300,
            value=150, step=5
        )
        distance = st.slider(
            "Distance to river (metres)",
            min_value=0, max_value=500,
            value=200, step=10
        )

        if st.button("Predict Flood Risk", type="primary"):
            st.session_state.pred_result = run_prediction(
                elevation, distance,
                st.session_state.pred_lat,
                st.session_state.pred_lon
            )

    with col_right:
        section_header("Map")


        risk = st.session_state.pred_result['risk_category'] if st.session_state.pred_result else "Low"

        m = folium.Map(
            location=[st.session_state.pred_lat, st.session_state.pred_lon],
            zoom_start=10
        )
        folium.Marker(
            location=[st.session_state.pred_lat, st.session_state.pred_lon],
            popup=st.session_state.pred_location,
            tooltip="Selected location",
            icon=folium.Icon(color=COLOUR_MAP.get(risk, "blue"), icon="info-sign")
        ).add_to(m)

        map_data = st_folium(m, width=450, height=380, returned_objects=["last_clicked"])

        # handle map click
        if map_data and map_data.get("last_clicked"):
            clicked_lat = map_data["last_clicked"]["lat"]
            clicked_lon = map_data["last_clicked"]["lng"]

            if (IRELAND_BOUNDS['lat_min'] <= clicked_lat <= IRELAND_BOUNDS['lat_max'] and
                    IRELAND_BOUNDS['lon_min'] <= clicked_lon <= IRELAND_BOUNDS['lon_max']):
                st.session_state.pred_lat = clicked_lat
                st.session_state.pred_lon = clicked_lon
                st.session_state.pred_region = get_region(clicked_lon)
                location_name = get_location_name(clicked_lat, clicked_lon)
                st.session_state.pred_location = location_name
                st.session_state.pred_result = run_prediction(
                    elevation, distance, clicked_lat, clicked_lon
                )
                info_box(f"Clicked: {location_name}")
            else:
                st.warning("Please click within Ireland.")

        # results below map
        if st.session_state.pred_result is not None:
            result = st.session_state.pred_result
            risk = result['risk_category']
            depth = result['flood_depth_m']

            col_a, col_b, col_c = st.columns(3)
            with col_a:
                metric_card("Risk", risk, "Category")
            with col_b:
                metric_card("Depth", f"{depth}m", "Predicted")
            with col_c:
                metric_card("Region", st.session_state.pred_region, "Area")

            if risk == "High":
                result_box("<strong>High flood risk.</strong> Low elevation and close to a river. Flood mitigation strongly recommended.")
                info_box("Insurance premiums will be higher. Construction requires flood mitigation planning.")
            elif risk == "Medium":
                result_box("<strong>Medium flood risk.</strong> Standard precautions advised during heavy rainfall.")
                info_box("Standard flood insurance recommended. Monitor OPW alerts at floodinfo.ie.")
            else:
                result_box("<strong>Low flood risk.</strong> Favourable elevation and distance from water.")
                info_box("Suitable for construction. Standard building regulations apply.")

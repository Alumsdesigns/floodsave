# Purpose: User inputs location by name or clicks map to get flood risk prediction
# Criteria: 4.1, 5.4, D7

import streamlit as st
import folium
import time
from streamlit_folium import st_folium
from geopy.geocoders import Nominatim
from geopy.exc import GeocoderTimedOut
from src.styles import section_header, info_box, metric_card, result_box
from src.ml_pipeline import predict_flood_risk
from src.data_management import get_location_name, get_elevation_metres, get_distance_to_river

IRELAND_BOUNDS = {
    'lat_min': 51.4, 'lat_max': 55.4,
    'lon_min': -10.5, 'lon_max': -5.4
}

COLOUR_MAP = {"High": "red", "Medium": "orange", "Low": "green"}

def geocode_location(location_name):
    """Convert Irish place name to lat/lng coordinates"""
    try:
        time.sleep(1)
        geolocator = Nominatim(user_agent="FloodSave/1.0")
        location = geolocator.geocode(
            f"{location_name}, Ireland",
            timeout=10,
            language='en'
        )
        if not location:
            location = geolocator.geocode(
                location_name,
                timeout=10,
                language='en',
                country_codes='ie'
            )
        if location:
            lat = location.latitude
            lon = location.longitude
            if (IRELAND_BOUNDS['lat_min'] <= lat <= IRELAND_BOUNDS['lat_max'] and
                    IRELAND_BOUNDS['lon_min'] <= lon <= IRELAND_BOUNDS['lon_max']):
                return lat, lon
        return None, None
    except Exception:
        return None, None


def get_region(longitude):
    """Derive Irish region from longitude"""
    if longitude < -8.0:
        return "West"
    elif longitude > -7.0:
        return "East"
    return "Midlands"


def run_prediction(elevation, distance, lat, lon):
    """Run ML prediction with given location features"""
    return predict_flood_risk({
        'elevation_m': elevation,
        'distance_to_river_m': distance,
        'latitude': lat,
        'longitude': lon
    })


def init_session_state():
    """Initialise all session state variables on first load"""
    defaults = {
        'pred_result': None,
        'pred_lat': 53.3,
        'pred_lon': -7.8,
        'pred_location': None,
        'pred_region': 'Midlands',
        'pred_elevation': None,
        'pred_distance': None,
        'last_input': '',
        'map_clicked': False
    }
    for key, value in defaults.items():
        if key not in st.session_state:
            st.session_state[key] = value


def page_risk_predictor():
    init_session_state()

    st.markdown('<div class="fs-title">Flood Risk Predictor</div>',
                unsafe_allow_html=True)
    st.markdown(
        '<div class="fs-subtitle">Search any Irish location or click the map</div>',
        unsafe_allow_html=True
    )

    col_left, col_right = st.columns([1, 1])

    # ── Left column — search and location details ──
    with col_left:
        section_header("Search Location")
        info_box("Type any Irish town or click the map. Elevation and river distance are fetched automatically.")

        location_input = st.text_input(
            "Town, city or area",
            placeholder="e.g. Athlone, Boyle, Cork, Galway...",
            value=st.session_state.last_input,
            key="location_text"
        )

        if location_input and location_input != st.session_state.get('prev_input', ''):
            with st.spinner("Finding location..."):
                lat, lon = geocode_location(location_input)
            if lat and lon:
                with st.spinner("Fetching elevation and river distance..."):
                    elevation = get_elevation_metres(lat, lon)
                    distance = get_distance_to_river(lat, lon)
                    location_name = get_location_name(lat, lon)
                st.session_state.pred_lat = lat
                st.session_state.pred_lon = lon
                st.session_state.pred_location = location_name
                st.session_state.pred_region = get_region(lon)
                st.session_state.pred_elevation = elevation
                st.session_state.pred_distance = distance
                st.session_state.prev_input = location_input
                st.session_state.last_input = location_input
                st.session_state.pred_result = None
            else:
                st.warning("Location not found in Ireland. Try a different spelling.")

        # show location details card when we have data
        if st.session_state.pred_elevation is not None:
            section_header("Location Details")

            if st.session_state.pred_location:
                info_box(f"Location: {st.session_state.pred_location}")

            col_a, col_b = st.columns(2)
            with col_a:
                metric_card(
                    "Elevation",
                    f"{st.session_state.pred_elevation}m",
                    "metres above sea level"
                )
            with col_b:
                river_val = st.session_state.pred_distance
                river_display = (
                    f"{river_val}m"
                    if river_val and river_val < 2000
                    else "Over 2km"
                )
                metric_card(
                    "Nearest River",
                    river_display,
                    "distance to waterway"
                )

            if st.button("Predict Flood Risk", type="primary"):
                with st.spinner("Running prediction..."):
                    st.session_state.pred_result = run_prediction(
                        st.session_state.pred_elevation,
                        st.session_state.pred_distance or 500,
                        st.session_state.pred_lat,
                        st.session_state.pred_lon
                    )
        else:
            info_box("Search a location or click the map to begin.")

    # ── Right column — map ──
    with col_right:
        section_header("Map")
        info_box("Click anywhere in Ireland to get flood risk for that location.")

        risk_colour = COLOUR_MAP.get(
            st.session_state.pred_result['risk_category']
            if st.session_state.pred_result else '', "blue"
        )

        m = folium.Map(
            location=[st.session_state.pred_lat, st.session_state.pred_lon],
            zoom_start=7,
            attributionControl=False
        )

        if st.session_state.pred_location:
            folium.Marker(
                location=[st.session_state.pred_lat, st.session_state.pred_lon],
                popup=st.session_state.pred_location,
                tooltip=st.session_state.pred_location,
                icon=folium.Icon(color=risk_colour, icon="info-sign")
            ).add_to(m)

        map_data = st_folium(
            m,
            width=450,
            height=420,
            returned_objects=["last_clicked"],
            key="main_map"
        )

        # handle map click — fetch data then rerun to update left column
        if map_data and map_data.get("last_clicked"):
            clicked_lat = map_data["last_clicked"]["lat"]
            clicked_lon = map_data["last_clicked"]["lng"]

            if (IRELAND_BOUNDS['lat_min'] <= clicked_lat <= IRELAND_BOUNDS['lat_max'] and
                    IRELAND_BOUNDS['lon_min'] <= clicked_lon <= IRELAND_BOUNDS['lon_max']):

                with st.spinner("Fetching location details..."):
                    elevation = get_elevation_metres(clicked_lat, clicked_lon)
                    distance = get_distance_to_river(clicked_lat, clicked_lon)
                    location_name = get_location_name(clicked_lat, clicked_lon)

                st.session_state.pred_lat = clicked_lat
                st.session_state.pred_lon = clicked_lon
                st.session_state.pred_region = get_region(clicked_lon)
                st.session_state.pred_location = location_name
                st.session_state.pred_elevation = elevation
                st.session_state.pred_distance = distance
                st.session_state.last_input = ''
                st.session_state.prev_input = ''
                st.session_state.pred_result = run_prediction(
                    elevation,
                    distance or 500,
                    clicked_lat,
                    clicked_lon
                )
                # force full rerender so left column updates
                st.rerun()
            else:
                st.warning("Click within Ireland to get a prediction.")

        # prediction results below map
        if st.session_state.pred_result is not None:
            result = st.session_state.pred_result
            risk = result['risk_category']
            depth = result['flood_depth_m']

            col_a, col_b, col_c = st.columns(3)
            with col_a:
                metric_card("Flood Risk", risk, "High / Medium / Low")
            with col_b:
                metric_card("Max Flood Depth", f"{depth}m", "metres")
            with col_c:
                metric_card("Region", st.session_state.pred_region,
                            "West / Midlands / East")
                
        if st.session_state.pred_distance and st.session_state.pred_distance >= 2000:
             info_box("Note: This location is over 2km from the nearest monitored waterway. Flood depth prediction is less reliable for locations far from rivers. The risk classification remains valid based on elevation and region.")

        if risk == "High":
            result_box("High flood risk. Low elevation and close to a river. Flood mitigation strongly recommended.")
            info_box("Insurance premiums will be higher. Construction requires flood mitigation planning. Monitor OPW alerts at floodinfo.ie.")
        elif risk == "Medium":
            result_box("Medium flood risk. Standard precautions advised during heavy rainfall.")
            info_box("Standard flood insurance recommended. Monitor OPW alerts at floodinfo.ie.")
        else:
            result_box("Low flood risk. Favourable elevation and distance from water.")
            info_box("Suitable for construction. Standard building regulations apply.")

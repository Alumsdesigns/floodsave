# app_pages/page_risk_predictor.py
# Interactive flood risk predictor — user searches by location name or map click
# Fetches real elevation from Open-Elevation API and river distance from OPW stations
# Criteria: 4.1 (data analytics conclusions), 5.4 (Streamlit dashboard), D7 (professional UX)

import streamlit as st
import folium
import time
from streamlit_folium import st_folium
from geopy.geocoders import Nominatim
from src.styles import section_header, info_box, metric_card, result_box,  back_to_top
from src.ml_pipeline import predict_flood_risk
from src.data_management import get_location_name, get_elevation_metres, get_distance_to_river

# Ireland geographic bounding box — prevents predictions outside Ireland
IRELAND_BOUNDS = {
    'lat_min': 51.4, 'lat_max': 55.4,
    'lon_min': -10.5, 'lon_max': -5.4
}

# map marker colours per risk level — defined once, used in two places
COLOUR_MAP = {"High": "red", "Medium": "orange", "Low": "green"}


def geocode_location(location_name):
    """Convert Irish place name to lat/lng using Nominatim API"""
    try:
        time.sleep(1) # nominatim rate limit — 1 request per second
        geolocator = Nominatim(user_agent="FloodSave/1.0")
        # try with Ireland suffix first for better accuracy
        location = geolocator.geocode(
            f"{location_name}, Ireland", timeout=10, language='en'
        )
        # fallback — restrict to Ireland country code without suffix
        if not location:
            location = geolocator.geocode(
                location_name, timeout=10, language='en', country_codes='ie'
            )
        if location:
            lat = location.latitude
            lon = location.longitude
            # validate result is within Ireland bounding box
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
    """Run ML prediction for a location"""
    return predict_flood_risk({
        'elevation_m': elevation,
        'distance_to_river_m': distance,
        'latitude': lat,
        'longitude': lon
    })


def init_session_state():
    """Initialise session state on first load"""
    defaults = {
        'pred_result': None,        # last prediction result dict
        'pred_lat': 53.3,           # default map centre — Ireland
        'pred_lon': -7.8,           # default map centre — Ireland
        'pred_location': None,      # location name string
        'pred_region': 'Midlands',  # West / Midlands / East
        'pred_elevation': None,     # elevation in metres from Open-Elevation API
        'pred_distance': None,      # distance to river in metres from OPW stations
        'last_input': '',           # last text input — cleared on map click
        'prev_input': '',           # tracks previous input to prevent re-fetch
        'last_click_key': '',       # tracks last map click to prevent rerun loop
        'map_clicked': False
    }
    for key, value in defaults.items():
        if key not in st.session_state:
            st.session_state[key] = value


def page_risk_predictor():
    init_session_state()

    # named anchor allows back to top button to scroll here
    st.markdown('<div id="floodsave-top"></div>', unsafe_allow_html=True)

    # page title and subtitle
    st.markdown('<div class="fs-title">Flood Risk Predictor</div>',
                unsafe_allow_html=True)
    st.markdown(
        '<div class="fs-subtitle">Search any Irish location or click the map</div>',
        unsafe_allow_html=True
    )

    # two column layout — search inputs left, map right
    col_left, col_right = st.columns([1, 1])

    # left column — search form and location details
    with col_left:
        section_header("Search Location")
        info_box("Type any Irish town or area and press Search. Or click anywhere on the map. Results update automatically.")

        # st.form prevents rerender on every keystroke
        # clear_on_submit=True clears the input after submission
        # fixes bug: old location staying in input after map click
        with st.form(key="location_form", clear_on_submit=True):
            location_input = st.text_input(
                "Town, city or area",
                placeholder="e.g. Athlone, Boyle, Cork, Galway..."
            )
            submitted = st.form_submit_button(
                "Search Location",
                use_container_width=True
            )

         # only process on form submit — not on every rerender
        if submitted and location_input:
            lat, lon = None, None
            elevation, distance, location_name = None, None, None

            # st.status shows step-by-step progress visible until complete
            with st.status("Searching for location...", expanded=True) as status:
                st.write("Finding location in Ireland...")
                lat, lon = geocode_location(location_input)

                if lat and lon:
                    st.write("Fetching elevation...")
                    elevation = get_elevation_metres(lat, lon)
                    st.write("Calculating river distance...")
                    distance = get_distance_to_river(lat, lon)
                    st.write("Getting location name...")
                    location_name = get_location_name(lat, lon)
                    status.update(
                        label="Location found",
                        state="complete",
                        expanded=False
                    )
                else:
                    status.update(
                        label="Location not found — try a different spelling",
                        state="error",
                        expanded=False
                    )

            # update session state and auto-run prediction
            if lat and lon:
                st.session_state.pred_lat = lat
                st.session_state.pred_lon = lon
                st.session_state.pred_location = location_name
                st.session_state.pred_region = get_region(lon)
                st.session_state.pred_elevation = elevation
                st.session_state.pred_distance = distance
                # auto-run prediction — no separate button needed
                st.session_state.pred_result = run_prediction(
                    elevation, distance or 500, lat, lon
                )
        # show location detail cards when data is available
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
                # show Over 2km when no river found within 2km search radius
                river_display = (
                    f"{river_val}m" if river_val and river_val < 2000
                    else "Over 2km"
                )
                metric_card("Nearest River", river_display, "distance to waterway")
        else:
            info_box("Search a location or click the map to begin.")

    # right column — interactive Folium map
    with col_right:
        section_header("Map")
        info_box("Click anywhere in Ireland to get flood risk for that location.")

        # marker colour reflects last prediction — blue before first prediction
        risk_colour = COLOUR_MAP.get(
            st.session_state.pred_result['risk_category']
            if st.session_state.pred_result else '',
            "blue"
        )

        # initialise Folium map centred on current location
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

        # render map and return click coordinates
        map_data = st_folium(
            m, width=450, height=420,
            returned_objects=["last_clicked"],
            key="main_map"
        )

        last_clicked = map_data.get("last_clicked") if map_data else None

        if last_clicked:
            clicked_lat = last_clicked["lat"]
            clicked_lon = last_clicked["lng"]
            # 4dp precision — detects clicks 11m apart
            # prevents same-area clicks being treated as identical
            click_key = f"{round(clicked_lat, 4)}_{round(clicked_lon, 4)}"

            # only process new clicks — prevents infinite rerun loop
            if click_key != st.session_state.last_click_key:
                st.session_state.last_click_key = click_key

                if (IRELAND_BOUNDS['lat_min'] <= clicked_lat <= IRELAND_BOUNDS['lat_max'] and
                        IRELAND_BOUNDS['lon_min'] <= clicked_lon <= IRELAND_BOUNDS['lon_max']):

                    with st.status("Fetching location data...", expanded=True) as status:
                        st.write("Getting elevation...")
                        elevation = get_elevation_metres(clicked_lat, clicked_lon)
                        st.write("Finding nearest river...")
                        distance = get_distance_to_river(clicked_lat, clicked_lon)
                        st.write("Getting location name...")
                        location_name = get_location_name(clicked_lat, clicked_lon)
                        status.update(
                            label="Done",
                            state="complete",
                            expanded=False
                        )

                    # update session state with clicked location
                    st.session_state.pred_lat = clicked_lat
                    st.session_state.pred_lon = clicked_lon
                    st.session_state.pred_region = get_region(clicked_lon)
                    st.session_state.pred_location = location_name
                    st.session_state.pred_elevation = elevation
                    st.session_state.pred_distance = distance
                    st.session_state.pred_result = run_prediction(
                        elevation, distance or 500, clicked_lat, clicked_lon
                    )
                    # force full rerender so left column cards update
                    st.rerun()

                else:
                    st.warning("Click within Ireland to get a prediction.")

    # results section — outside both columns so it spans full width
    if st.session_state.pred_result is not None:
        result = st.session_state.pred_result
        risk = result['risk_category']
        depth = result['flood_depth_m']

        st.markdown("---")
        # three result metric cards
        col_a, col_b, col_c = st.columns(3)
        with col_a:
            metric_card("Flood Risk", risk, "High / Medium / Low")
        with col_b:
            metric_card("Max Flood Depth", f"{depth}m", "metres")
        with col_c:
            metric_card("Region", st.session_state.pred_region,
                        "West / Midlands / East")

        # accuracy warning when location is far from monitored rivers
        if st.session_state.pred_distance and st.session_state.pred_distance >= 2000:
            info_box("Note: This location is over 2km from the nearest monitored waterway. Flood depth prediction is less reliable here. Risk classification remains valid based on elevation and region.")

         # result box and advice based on predicted risk level
        if risk == "High":
            result_box("High flood risk. Low elevation and close to a river. Flood mitigation strongly recommended.")
            info_box("Insurance premiums will be higher. Construction requires flood mitigation planning. Monitor OPW alerts at floodinfo.ie.")
        elif risk == "Medium":
            result_box("Medium flood risk. Standard precautions advised during heavy rainfall.")
            info_box("Standard flood insurance recommended. Monitor OPW alerts at floodinfo.ie.")
        else:
            result_box("Low flood risk. Favourable elevation and distance from water.")
            info_box("Suitable for construction. Standard building regulations apply.")

    # back to top button — fixed position bottom right on all screen sizes
    back_to_top()
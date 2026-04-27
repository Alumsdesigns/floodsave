# src/data_management.py
# Single source of truth for all data loading and external API calls
# All dashboard pages import from here — no direct CSV or API calls in pages
# Criteria: 7.1 (data collection), 7.2 (data preparation)

import pandas as pd
import os
import time
import requests
from functools import lru_cache


def load_clean_data():
    """Load cleaned OPW station dataset from outputs/v1/cleaned_data.csv"""
    path = os.path.join('outputs', 'v1', 'cleaned_data.csv')
    return pd.read_csv(path)


def load_featured_data():
    """Load feature-engineered dataset from outputs/v1/featured_data.csv"""
    path = os.path.join('outputs', 'v1', 'featured_data.csv')
    return pd.read_csv(path)


@lru_cache(maxsize=256)
def get_location_name(latitude, longitude):
    """
    Reverse geocode lat/lng to nearest Irish place name.
    Uses OSM Nominatim API — free, no key required.
    Results cached by coordinate — same location never hits API twice.
    Pass coordinates rounded to 3-4dp before calling.
    """
    try:
        time.sleep(1)  # nominatim rate limit — 1 request per second
        url = "https://nominatim.openstreetmap.org/reverse"
        params = {
            'lat': latitude,
            'lon': longitude,
            'format': 'json',
            'zoom': 14,              # town/neighbourhood level
            'addressdetails': 1,
            'accept-language': 'en'  # force English response
        }
        headers = {'User-Agent': 'FloodSave/1.0'}
        response = requests.get(url, params=params, headers=headers, timeout=5)
        data = response.json()
        address = data.get('address', {})

        # use country_code not country name — reliable across languages
        if address.get('country_code', '').lower() != 'ie':
            return "Location outside Ireland"

        # prioritise most specific place name available
        town = (
            address.get('road') or
            address.get('hamlet') or
            address.get('village') or
            address.get('town') or
            address.get('city_district') or
            address.get('suburb') or
            address.get('city') or
            address.get('municipality') or
            address.get('county') or
            'Unknown location'
        )
        county = address.get('county', '')

        if county and county.lower() not in town.lower():
            return f"{town}, {county}"
        return town

    except Exception:
        # return coordinates as fallback — never show generic error to user
        return f"Location at {round(latitude, 4)}, {round(longitude, 4)}"


def get_elevation_metres(latitude, longitude):
    """
    Fetch real elevation in metres from Open-Elevation API.
    Free, no key required, global coverage including Ireland.
    Falls back to latitude-based estimate if API is unavailable.
    """
    try:
        url = "https://api.open-elevation.com/api/v1/lookup"
        params = {'locations': f"{latitude},{longitude}"}
        response = requests.get(url, params=params, timeout=5)
        return round(response.json()['results'][0]['elevation'], 1)
    except Exception:
        # linear estimate from latitude — higher latitude = higher ground in Ireland
        return round(((latitude - 51.4) / (55.4 - 51.4)) * 200 + 50, 1)


def get_distance_to_river(latitude, longitude):
    """
    Calculate distance in metres to nearest OPW hydrometric station.
    OPW stations are placed on rivers — this approximates distance to water.
    Uses haversine formula on Earth radius 6371km.
    No external API — uses the 457 stations already in the dataset.
    """
    try:
        from math import radians, sin, cos, sqrt, atan2

        df = load_featured_data()
        R = 6371000  # earth radius in metres
        min_distance = 999999

        for _, row in df.iterrows():
            lat1 = radians(latitude)
            lat2 = radians(row['latitude'])
            dlat = radians(row['latitude'] - latitude)
            dlon = radians(row['longitude'] - longitude)
            a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
            distance = int(R * 2 * atan2(sqrt(a), sqrt(1-a)))
            min_distance = min(min_distance, distance)

        return min_distance

    except Exception:
        return 2000  # default if calculation fails
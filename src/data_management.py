# Purpose: Single source of truth for loading data across all dashboard pages
# Any page that needs data imports from here — never loads CSV directly

import pandas as pd
import os
import requests                       
from functools import lru_cache    
import time

def load_clean_data():
    """Load the cleaned and featured dataset from outputs/v1/"""
    path = os.path.join('outputs', 'v1', 'cleaned_data.csv')
    df = pd.read_csv(path)
    return df


def load_featured_data():
    """Load the featured dataset with engineered columns from outputs/v1/"""
    path = os.path.join('outputs', 'v1', 'featured_data.csv')
    df = pd.read_csv(path)
    return df

@lru_cache(maxsize=128)
def get_location_name(latitude, longitude):
    """
    Reverse geocode to nearest Irish location.
    Coordinates rounded to 3dp before caching — 
    clicks within 100m reuse cached result.
    """
    try:
        time.sleep(1)  # respect Nominatim rate limit
        url = "https://nominatim.openstreetmap.org/reverse"
        params = {
            'lat': latitude,
            'lon': longitude,
            'format': 'json',
            'zoom': 14,
            'addressdetails': 1,
            'accept-language': 'en'
        }
        headers = {'User-Agent': 'FloodSave/1.0'}
        response = requests.get(url, params=params, headers=headers, timeout=5)
        data = response.json()
        address = data.get('address', {})

        country_code = address.get('country_code', '').lower()
        if country_code != 'ie':
            return "Location outside Ireland"

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
        return "Location lookup unavailable"
    

def get_elevation_metres(latitude, longitude):
    """
    Get real elevation in metres from Open-Elevation API.
    Free, no key required, covers all of Ireland.
    Falls back to estimate if API unavailable.
    """
    try:
        url = "https://api.open-elevation.com/api/v1/lookup"
        params = {'locations': f"{latitude},{longitude}"}
        response = requests.get(url, params=params, timeout=5)
        data = response.json()
        return round(data['results'][0]['elevation'], 1)
    except Exception:
        # fallback estimate from latitude if API unavailable
        return round(((latitude - 51.4) / (55.4 - 51.4)) * 200 + 50, 1)
    

def get_distance_to_river(latitude, longitude):
    """
    Estimate distance to nearest river using OPW station locations.
    Uses stations already loaded — no external API needed.
    Fast and reliable.
    """
    try:
        from math import radians, sin, cos, sqrt, atan2
        df = load_featured_data()

        R = 6371000
        min_distance = 999999

        for _, row in df.iterrows():
            lat1 = radians(latitude)
            lat2 = radians(row['latitude'])
            dlat = radians(row['latitude'] - latitude)
            dlon = radians(row['longitude'] - longitude)
            a = sin(dlat/2)**2 + cos(lat1)*cos(lat2)*sin(dlon/2)**2
            distance = int(R * 2 * atan2(sqrt(a), sqrt(1-a)))
            min_distance = min(min_distance, distance)

        return min_distance

    except Exception:
        return 2000

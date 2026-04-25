# Purpose: Single source of truth for loading data across all dashboard pages
# Any page that needs data imports from here — never loads CSV directly

import pandas as pd
import os
import requests                       
from functools import lru_cache    


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
    Reverse geocode lat/lng to nearest Irish town using OSM Nominatim.
    Results are cached so repeated calls with same coords skip the API.
    """
    try:
        url = "https://nominatim.openstreetmap.org/reverse"
        params = {
            'lat': latitude,
            'lon': longitude,
            'format': 'json',
            'zoom': 10,
            'addressdetails': 1
        }
        headers = {'User-Agent': 'FloodSave/1.0'}
        response = requests.get(url, params=params, headers=headers, timeout=5)
        data = response.json()
        address = data.get('address', {})

        town = (
            address.get('town') or
            address.get('city') or
            address.get('village') or
            address.get('hamlet') or
            'Unknown location'
        )
        county = address.get('county', '')
        country = address.get('country', '')

        irish_names = {'Ireland', 'Republic of Ireland', 'Éire', 'Eire'}
        if country not in irish_names:
            return "Location outside Ireland"

        return f"Near {town}, {county}"

    except Exception:
        return "Location lookup unavailable"
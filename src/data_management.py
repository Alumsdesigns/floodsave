# src/data_management.py
# Purpose: Single source of truth for loading data across all dashboard pages
# Any page that needs data imports from here — never loads CSV directly

import pandas as pd
import os


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
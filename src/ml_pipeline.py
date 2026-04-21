# src/ml_pipeline.py
# Purpose: Load trained models and run predictions for dashboard pages
# Any page that needs predictions imports from here — never loads pkl directly

import joblib
import pandas as pd
import os


def load_classification_model():
    """Load the trained Random Forest classification pipeline"""
    path = os.path.join('outputs', 'v1', 'classification_pipeline.pkl')
    return joblib.load(path)


def load_regression_model():
    """Load the trained Random Forest regression pipeline"""
    path = os.path.join('outputs', 'v1', 'regression_pipeline.pkl')
    return joblib.load(path)


def predict_flood_risk(input_dict):
    """
    Predict flood risk category and depth for a given location.
    
    input_dict: dictionary with keys:
        elevation_m, distance_to_river_m, latitude, longitude
    
    Returns: dict with risk_category and flood_depth_m
    """
    clf = load_classification_model()
    reg = load_regression_model()

    input_df = pd.DataFrame([input_dict])

    risk_category = clf.predict(input_df)[0]
    flood_depth = reg.predict(input_df)[0]

    return {
        'risk_category': risk_category,
        'flood_depth_m': round(float(flood_depth), 2)
    }
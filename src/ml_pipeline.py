# src/ml_pipeline.py
# Loads trained Random Forest pipelines and runs predictions
# All dashboard pages import predict_flood_risk from here
# Never load pkl files directly in dashboard pages
# Criteria: 5.1 (modelling), 5.2 (evaluation), 5.4 (dashboard prediction)

import joblib
import pandas as pd
import os


def load_classification_model():
    """Load trained Random Forest classifier from outputs/v1/"""
    path = os.path.join('outputs', 'v1', 'classification_pipeline.pkl')
    return joblib.load(path)


def load_regression_model():
    """Load trained Random Forest regressor from outputs/v1/"""
    path = os.path.join('outputs', 'v1', 'regression_pipeline.pkl')
    return joblib.load(path)


def predict_flood_risk(input_dict):
    """
    Run classification and regression prediction for a location.

    Args:
        input_dict: dict with keys elevation_m, distance_to_river_m,
                    latitude, longitude

    Returns:
        dict with risk_category (High/Medium/Low) and flood_depth_m (float)
    """
    clf = load_classification_model()
    reg = load_regression_model()

    # convert input dict to single-row dataframe for sklearn pipeline
    input_df = pd.DataFrame([input_dict])

    risk_category = clf.predict(input_df)[0]
    flood_depth = reg.predict(input_df)[0]

    return {
        'risk_category': risk_category,
        'flood_depth_m': round(float(flood_depth), 2)
    }
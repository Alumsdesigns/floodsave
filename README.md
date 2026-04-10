
# FloodSave — Flood Risk Prediction System

## Overview
FloodSave is an intelligent flood risk prediction platform that classifies 
flood risk and predicts flood depth for any location using geographic 
and environmental data. Built initially for Ireland with a scalable 
architecture designed for expansion.

## Current Coverage
- 🇮🇪 Ireland (active) — OPW flood zone data

## Dataset Content
The current dataset is sourced from the Irish Office of Public Works 
(OPW) via floodinfo.ie and data.gov.ie. It contains flood zone 
classifications, river monitoring data, and property-level risk 
indicators across Irish counties.

Each row represents a geographic location with the following attributes:
- Elevation above sea level (metres)
- Distance to nearest river or water body (metres)
- County and region
- OPW flood zone classification
- Historical flood depth records

## Business Requirements
1. The client wants to understand which geographic and environmental 
   features correlate most strongly with flood risk classification.
2. The client wants to predict the flood risk category 
   (High / Medium / Low) for any location given its

## Tree Structure

floodiq/
│
├── app.py                 # Streamlit entry point, the app runs, dashboard starts here
├── requirements.txt       # Python packages list
├── .gitignore             # Tells git what NOT to track i.e. venv, cache, raw data files
├── README.md              # Project documentation (we write this now)
│
├── app_pages/
│   └── __init__.py        # Empty file, makes folder a Python package
│
├── src/
│   └── __init__.py        # Same as above
│
├── inputs/
│   └── datasets/
│       └── raw/
│           └── .gitkeep   # Empty file, just holds the folder in git
│
├── outputs/
│   └── v1/
│       └── .gitkeep       # Same as above
│
└── jupyter_notebooks/     # Notebooks go here later

## Libraries & Purpose

run 
> pip install streamlit scikit-learn matplotlib seaborn plotly scipy

### Streamlit

Used to build the interactive dashboard interface, allowing users to explore data, models, and visualisations in real time.

### scikit-learn

Core machine learning library used for:

Training models (e.g. Random Forest Classifier & Regressor)
Hyperparameter tuning with GridSearchCV
Model evaluation and preprocessing

### Matplotlib

Provides foundational plotting capabilities for generating static charts and visualisations within notebooks.

### Seaborn

Built on top of Matplotlib, used for:

Enhanced statistical visualisations
Heatmaps, boxplots, and distribution plots
Cleaner and more interpretable graphics

### Plotly

Enables interactive visualisations in the dashboard:

Hover, zoom, and dynamic filtering
Rich, user-friendly charts for better insights

### SciPy

Used for statistical analysis, including:

Hypothesis testing (e.g. Chi-square tests, t-tests)
Supporting validation of analytical findings
Summary

These libraries together power:

Data visualisation (static + interactive)
Machine learning modelling and optimisation
Statistical analysis and hypothesis testing
A user-friendly interactive dashboard


Streamlit – Builds the interactive dashboard for data exploration and model insights.
scikit-learn – Trains and evaluates ML models (e.g. Random Forest) and supports hyperparameter tuning with GridSearchCV.
Matplotlib – Provides core plotting functionality for static visualisations.
Seaborn – Enhances statistical visualisations (e.g. heatmaps, distributions).
Plotly – Delivers interactive charts with zoom, hover, and filtering in the dashboard.
SciPy – Performs statistical tests (e.g. t-tests, chi-square) for hypothesis validation.
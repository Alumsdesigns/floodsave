
# FloodSave — Flood Risk Prediction System

## Overview
FloodSave is an intelligent flood risk prediction platform that classifies 
flood risk and predicts flood depth for any location using geographic 
and environmental data. Built initially for Ireland with a scalable 
architecture designed for expansion.

---

## Current Coverage
 🇮🇪 Ireland (active) — OPW flood zone data

---

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

---

## Business Requirements
1. The client wants to understand which geographic and environmental 
   features correlate most strongly with flood risk classification.
2. The client wants to predict the flood risk category 
   (High / Medium / Low) for any Irish location given its attributes.
3. The client wants to predict the expected flood depth in metres 
   for a given location and understand the geographic extent of 
   flood risk in their area, enabling informed decisions about 
   safety, insurance, and evacuation planning.

---

## Future Enhancements cuurently out of scope

## Future 
- Real-time rainfall API integration
- Live flood spread calculation
- Safe route navigation by foot
- Safe route navigation by road
- UK and East Africa coverage


--- 

## User Stories
- As a construction site manager, I want to enter a location and see 
  its flood risk classification so I can assess site safety before 
  breaking ground.
- As an insurance underwriter, I want to predict flood depth for a 
  property so I can price flood risk premiums accurately.
- As a member of the public, I want to understand the flood risk in 
  my area during heavy rainfall so I can make informed safety decisions.

--- 
## Hypotheses
1. Properties with elevation below 10 metres have significantly higher 
   flood risk classification than properties above 10 metres.
   - Validation: Chi-square test on elevation_category vs flood_risk_class

2. Distance to nearest river is the strongest predictor of flood risk, 
   with properties within 500m having higher risk.
   - Validation: Feature importance analysis and independent t-test

3. Western counties (Galway, Mayo, Clare) have higher average predicted 
   flood depth than Eastern counties due to higher rainfall.
   - Validation: Independent t-test on county_region vs max_flood_depth

---

## ML Business Case

### Classification Task
- **Aim:** Predict flood risk category (High / Medium / Low) for any 
  Irish location based on geographic and environmental features
- **Learning method:** Supervised classification using Random Forest
- **Ideal outcome:** Model correctly classifies flood risk with at least 
  75% accuracy on unseen test data
- **Success metric:** Accuracy score above 0.75, F1 score above 0.70
- **Failure metric:** Accuracy below 0.75 — model not deployed
- **Model output:** Risk category label displayed on dashboard predictor page
- **Training data:** OPW flood zone data with engineered features

---

### Regression Task
- **Aim:** Predict expected flood depth in metres for a given location
- **Learning method:** Supervised regression using Random Forest Regressor
- **Ideal outcome:** Model predicts flood depth within acceptable margin
- **Success metric:** R² score above 0.75 on test set
- **Failure metric:** R² below 0.75 — model performance noted on dashboard
- **Model output:** Predicted depth in metres shown on dashboard
- **Training data:** Historical flood depth records from OPW dataset

---

## Rationale to Map Business Requirements to ML Tasks

| Business Requirement | Visualisation / ML Task |
|----------------------|------------------------|
| BR1 — Understand feature correlations | Correlation heatmap, scatter plots, feature importance chart |
| BR2 — Predict flood risk category | Random Forest Classifier — Classification pipeline |
| BR3 — Predict flood depth and area extent | Random Forest Regressor + Folium map overlay |

---

## Dashboard Design

- **Page 1 — Project Summary:** Overview of FloodSave, dataset description, 
  business requirements. Answers BR1.
- **Page 2 — Flood Risk Study:** Histogram, scatter plot, heatmap and 
  boxplot showing correlations between features and flood risk. Answers BR1.
- **Page 3 — Hypothesis Validation:** Three hypotheses with statistical 
  test results, p-values and conclusions. Answers BR2 and BR3.
- **Page 4 — Risk Predictor:** Input widgets for location attributes, 
  returns risk classification, flood depth prediction and folium map. 
  Answers BR2 and BR3.
- **Page 5 — Model Performance:** Confusion matrix, classification report, 
  R² score, Actual vs Predicted plot and feature importance. Answers BR2 and BR3.

---

## Tree Structure

floodsave/
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

## Libraries

| Library | Purpose |
|---------|---------|
| Streamlit | Interactive dashboard interface |
| scikit-learn | Random Forest models, GridSearchCV, preprocessing |
| Matplotlib | Static charts and plots in notebooks |
| Seaborn | Statistical visualisations — heatmaps, boxplots |
| Plotly | Interactive charts on dashboard |
| SciPy | Statistical tests — chi-square and t-tests |
| Folium | Static flood zone map on predictor page |

---



## Libraries & Purpose

run 
> pip install streamlit scikit-learn matplotlib seaborn plotly scipy

### Streamlit

Builds the interactive dashboard for data exploration and model insights. Used to build the interactive dashboard interface, allowing users to explore data, models, and visualisations in real time.

### scikit-learn

 Core machine learning library used for:

Training models (e.g. Random Forest Classifier & Regressor)
Supports Hyperparameter tuning with GridSearchCV
Model evaluation and preprocessing

### Matplotlib

Provides foundational core plotting capabilities for generating static charts and visualisations within notebooks.

### Seaborn

Built on top of Matplotlib, used for:

Enhanced statistical visualisations
Example heatmaps, boxplots, and distribution plots
Cleaner and more interpretable graphics

### Plotly

Enables interactive visualisations in the dashboard:
Delivers interactive charts with zoom, hover, and dynamic filtering in the dashboard. These are rich, user-friendly charts for better insights


### SciPy

Performs statistical tests (e.g. t-tests, chi-square) for hypothesis validation. Used for statistical analysis, including:

Hypothesis testing (e.g. Chi-square tests, t-tests)
Supporting validation of analytical findings


#### Summary

These libraries together power:

Data visualisation (static + interactive)
Machine learning modelling and optimisation
Statistical analysis and hypothesis testing
A user-friendly interactive dashboard




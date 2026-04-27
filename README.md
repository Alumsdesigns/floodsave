# FloodSave — Flood Risk Prediction System

**View the Floodsave Web Application:** [View Deployed Site](https://floodsave-bf0f49c3b6af.herokuapp.com/) 
Enjoy learning more about flood risks in different areas

---

## Table of Contents

1. [Overview](#overview)
2. [Value and Impact](#value-and-impact)
3. [CRISP-DM Process](#crisp-dm-process)
4. [UX Design Decisions](#ux-design-decisions)
5. [File Structure](#file-structure)
6. [Dataset Content](#dataset-content)
7. [Business Requirements](#business-requirements)
8. [User Stories](#user-stories)
9. [User Story to ML Task Mapping](#user-story-to-ml-task-mapping)
10. [Hypotheses and Validation Results](#hypotheses-and-validation-results)
11. [ML Business Case](#ml-business-case)
12. [Rationale to Map Business Requirements to ML Tasks](#rationale-to-map-business-requirements-to-ml-tasks)
13. [Dashboard Design](#dashboard-design)
14. [Tech Stack](#tech-stack)
15. [Libraries](#libraries)
16. [Bug Fixes](#bug-fixes)
17. [Known Limitations](#known-limitations)
18. [Future Enhancements](#future-enhancements)

---

## Overview
FloodSave is an intelligent flood risk prediction platform that classifies
flood risk and predicts flood depth for any Irish location using geographic
and environmental data. Built on real-time OPW hydrometric station data
with a scalable architecture designed for future expansion.

---

## Value and Impact

FloodSave addresses a genuine gap in the Irish market. No existing tool
provides property-level flood risk intelligence built specifically on Irish
OPW data. The platform delivers measurable value across four sectors:

| Sector | Problem Solved | Impact |
|--------|---------------|--------|
| Construction | Site risk unknown before breaking ground | Reduces planning delays and insurance costs |
| Insurance | Flood depth estimates rely on generic European models | Enables accurate Irish property premium pricing |
| Local Government | Emergency planning uses outdated static maps | Live station data supports dynamic response planning |
| Public | No accessible tool to check personal flood risk | Empowers informed safety decisions during heavy rainfall |

The Western counties of Ireland (Galway, Mayo, Clare) receive significantly
higher rainfall than Eastern counties due to Atlantic weather systems hitting
the coast before reaching the rain shadow created by the Wicklow, Silvermine
and Slieve Bloom mountain ranges. FloodSave quantifies this difference
statistically — Western stations show mean flood depth of 1.028m versus
0.767m in Eastern counties (p = 0.0007).

---

## CRISP-DM Process

| Phase | Implementation |
|-------|---------------|
| Business Understanding | Business requirements, user stories, ML business case |
| Data Understanding | Notebook 01 data collection, Notebook 04 EDA |
| Data Preparation | Notebook 02 cleaning, Notebook 03 feature engineering |
| Modelling | Notebook 06 classification, Notebook 07 regression |
| Evaluation | Confusion matrix, R2 score, hypothesis tests |
| Deployment | Streamlit Community Cloud |

---

## UX Design Decisions

The dashboard follows these UX principles:

- **Information hierarchy:** Summary page first, predictor last — users
  understand context before making predictions
- **Consistency:** Same card components, colour scheme and layout
  pattern across all 5 pages via shared src/styles.py
- **User feedback:** Status messages and spinners confirm every action
  is processing — users are never left waiting without feedback
- **Accessibility:** Colour contrast meets WCAG AA standard (minimum 4.5:1 ratio).
  All charts include text labels and hover tooltips for screen reader compatibility
- **Mobile responsive:** Single column layout on screens below 1024px.
  Sidebar collapses to hamburger menu on mobile
- **User control:** No auto-playing content. All predictions triggered
  by explicit user action

---

## File Structure

```
floodsave/
├── app.py
├── requirements.txt
├── Procfile
├── runtime.txt
├── setup.sh
├── README.md
├── app_pages/
│   ├── __init__.py
│   ├── page_summary.py
│   ├── page_flood_risk_study.py
│   ├── page_hypothesis_validation.py
│   ├── page_risk_predictor.py
│   └── page_model_performance.py
├── src/
│   ├── __init__.py
│   ├── data_management.py
│   ├── ml_pipeline.py
│   └── styles.py
├── jupyter_notebooks/
│   ├── 01_data_collection.ipynb
│   ├── 02_data_cleaning.ipynb
│   ├── 03_feature_engineering.ipynb
│   ├── 04_data_visualisation.ipynb
│   ├── 05_hypothesis_validation.ipynb
│   ├── 06_modeling_classification.ipynb
│   └── 07_modeling_regression.ipynb
└── docs/
    ├── crisp_dm.md
    ├── hypothesis_validation.md
    ├── ml_pipeline.md
    └── user_flow.md
```

---

## Dataset Content

The dataset is sourced from the Irish Office of Public Works (OPW)
Real-Time Water Levels API at waterlevel.ie/geojson — a live endpoint
updated continuously by OPW hydrometric data loggers across Ireland.

**Data freshness:** The OPW API provides real-time readings. The station
list was pulled in April 2026 and contains 457 active monitoring stations.
Each station transmits water level data via GPRS telemetry at regular
intervals. The dataset is licensed under Creative Commons CC-BY 4.0.

Each row represents one OPW hydrometric monitoring station with the
following attributes:

| Column | Description |
|--------|-------------|
| name | Station name e.g. Sandy Mills |
| ref | OPW station reference number |
| longitude | GPS longitude coordinate |
| latitude | GPS latitude coordinate |
| region | Derived region — West, Midlands, East |
| elevation_m | Estimated elevation in metres |
| distance_to_river_m | Distance to nearest OPW station in metres |
| flood_risk | Classified risk — High, Medium, Low |
| flood_depth_m | Estimated flood depth in metres |
| elevation_category | Binned elevation — Low, Medium, High |
| distance_category | Binned distance — Very Close, Close, Far |
| flood_risk_encoded | Numeric encoding — High=2, Medium=1, Low=0 |

---

## Business Requirements

1. The client wants to understand which geographic and environmental
   features correlate most strongly with flood risk classification.
2. The client wants to predict the flood risk category
   (High / Medium / Low) for any Irish location given its attributes.
3. The client wants to predict the expected flood depth in metres
   for a given location and understand the geographic extent of flood
   risk in their area, enabling informed decisions about safety,
   insurance, and evacuation planning.

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

## User Story to ML Task Mapping

| User Story | Dashboard Page | ML Task |
|-----------|---------------|---------|
| Construction manager checks site risk | Risk Predictor | Classification pipeline |
| Insurance underwriter predicts flood depth | Risk Predictor | Regression pipeline |
| Public checks area flood risk | Risk Predictor | Classification + Folium map |
| Analyst studies feature correlations | Flood Risk Study | EDA visualisations |
| Researcher validates flood hypotheses | Hypothesis Validation | Statistical tests |

---

## Hypotheses and Validation Results

### Hypothesis 1 — Elevation and Flood Risk
Properties with elevation below 10 metres have significantly higher
flood risk classification than properties above 10 metres.

- Test: Chi-square test on elevation_category vs flood_risk
- Result: SUPPORTED
- p-value: 0.0000
- Finding: Low elevation stations have significantly higher flood risk.
  The relationship between elevation category and flood risk category
  is statistically significant beyond any reasonable threshold.

### Hypothesis 2 — Distance to River and Flood Risk
Distance to nearest river is the strongest predictor of flood risk,
with stations within 100m having significantly higher risk.

- Test: Independent t-test on distance group vs flood_risk_encoded
- Result: SUPPORTED
- p-value: 0.0000
- Finding: Stations within 100m of a river have mean risk score 1.19
  versus 0.74 for stations beyond 100m — a statistically significant
  difference confirming proximity to water as a key risk driver.

### Hypothesis 3 — Western vs Eastern Flood Depth
Western counties have higher average predicted flood depth than
Eastern counties due to higher Atlantic rainfall.

- Test: Independent t-test on region vs flood_depth_m
- Result: SUPPORTED
- p-value: 0.0007
- Finding: Western stations mean depth 1.028m versus Eastern 0.767m.
  The difference is explained by Atlantic weather systems hitting the
  Western coast before reaching the rain shadow of the Wicklow and
  Silvermine mountain ranges.

---

## ML Business Case

### Classification Task
- **Aim:** Predict flood risk category (High / Medium / Low) for any
  Irish location based on geographic and environmental features
- **Learning method:** Supervised multiclass classification using Random Forest ensemble
- **Ideal outcome:** Model correctly classifies flood risk with at least 75% accuracy
- **Success metric:** Accuracy score above 0.75, F1 score above 0.70
- **Failure metric:** Accuracy below 0.75 — model not deployed
- **Model output:** Risk category label displayed on dashboard predictor page
- **Training data:** 457 OPW station records with engineered features
- **Heuristics:** Elevation below sea level and proximity to rivers
  are known flood risk indicators — used to validate model outputs
- **ML terminology:** Supervised multiclass classification, ensemble method,
  bagging, out-of-bag error estimation, GridSearchCV hyperparameter optimisation

### Regression Task
- **Aim:** Predict expected flood depth in metres for a given location
- **Learning method:** Supervised regression using Random Forest Regressor
- **Ideal outcome:** Model predicts flood depth with R2 above 0.75
- **Success metric:** R2 score above 0.75 on test set
- **Failure metric:** R2 below 0.75 — limitation documented on dashboard
- **Model output:** Predicted depth in metres shown on dashboard
- **Training data:** 457 OPW station records with flood depth targets
- **ML terminology:** Supervised regression, ensemble method, mean absolute error,
  R2 coefficient of determination

---

## Rationale to Map Business Requirements to ML Tasks

| Business Requirement | Visualisation / ML Task |
|----------------------|------------------------|
| BR1 — Understand feature correlations | Correlation heatmap, scatter plots, feature importance chart |
| BR2 — Predict flood risk category | Random Forest Classifier — Classification pipeline |
| BR3 — Predict flood depth and area extent | Random Forest Regressor + Folium interactive map |

---

## Dashboard Design

- **Project Summary** — Text overview of FloodSave, dataset description
  with 4 metric cards, business requirements mapped to 3 cards, target
  user groups. Answers BR1.
- **Flood Risk Study** — 4 interactive Plotly charts: histogram of
  elevation distribution, scatter of elevation vs flood depth,
  correlation heatmap, boxplot of flood depth by risk category.
  All charts have hover tooltips and plain English explanations.
  Answers BR1.
- **Hypothesis Validation** — 3 hypotheses each with claim, test used,
  p-value metric card, result metric card and plain English finding.
  Answers BR1, BR2, BR3.
- **Risk Predictor** — Location search form, interactive Folium map
  with click-to-predict, real elevation from Open-Elevation API,
  river distance from OPW station proximity, auto-prediction with
  risk category and flood depth result cards. Answers BR2 and BR3.
- **Model Performance** — Classification metrics (accuracy, precision,
  recall, F1), confusion matrix heatmap, regression R2 and MAE,
  feature importance bar chart, hyperparameter tuning table with
  rationale. Answers BR2 and BR3.

---

## Tech Stack

| Layer | Technology | Purpose |
|-------|-----------|---------|
| Language | Python 3.13 | Core development language |
| Dashboard | Streamlit | Interactive web application |
| ML | scikit-learn | Random Forest classifier and regressor |
| Data | pandas, numpy | Data manipulation and analysis |
| Visualisation | Plotly, Matplotlib, Seaborn | Interactive and static charts |
| Statistics | SciPy | Chi-square and t-tests |
| Mapping | Folium, streamlit-folium | Interactive map with click-to-predict |
| Geocoding | Geopy Nominatim | Convert location name to coordinates |
| Elevation | Open-Elevation API | Real elevation data for any Irish location |
| River Distance | OPW station proximity | Haversine distance to nearest OPW station |
| Version Control | Git and GitHub | Code versioning and collaboration |
| Deployment | Streamlit Community Cloud | Free public hosting |

---

## Libraries

| Library | Purpose |
|---------|---------|
| streamlit | Interactive dashboard interface |
| scikit-learn | Random Forest models, GridSearchCV, preprocessing |
| matplotlib | Static charts and plots in notebooks |
| seaborn | Statistical visualisations in notebooks |
| plotly | Interactive charts on dashboard |
| scipy | Statistical tests — chi-square and t-tests |
| folium | Interactive map on predictor page |
| streamlit-folium | Renders Folium map inside Streamlit |
| geopy | Geocodes location names to coordinates |
| joblib | Saves and loads trained model pipelines |
| pandas | Data manipulation and CSV handling |
| numpy | Numerical computation |

---

## Bug Fixes

| Bug | Fix Applied |
|-----|------------|
| Streamlit rerender clearing prediction results | Fixed using st.session_state to persist results |
| venv broken after folder rename | Deleted and recreated venv |
| Notebook JSON error on empty file | Replaced touch command with valid JSON scaffold |
| Location outside Ireland for valid Irish locations | Changed country name check to country_code ie |
| Matplotlib deprecation warning on boxplot labels | Renamed labels to tick_labels |
| Results not showing after map click | Moved results block outside columns to span full width |
| Infinite rerun loop on map click | Added click_key tracking to only process new clicks |
| Old location data showing when new location loads | Replaced text_input with st.form — only triggers on submit |
| Input box not clearing when map clicked | Form clear_on_submit=True handles clearing natively |
| Same area clicks being skipped | Increased click precision from 3dp to 4dp |
| Rate limiting error 429 from Nominatim | Added time.sleep(1) to respect rate limit |
| River distance stuck at 200m default | Replaced Overpass API with OPW station haversine calculation |
| Location lookup unavailable for small Irish towns | Switched to country_code ie check for reliability |

---

## Known Limitations

- Browser console shows iframe sandbox warnings from the streamlit-folium
  library. This is a known third-party issue and does not affect functionality
- Map marker updates after full page rerender, not in real time while typing
- Flood depth predictions are most accurate for locations near monitored rivers.
  For locations over 2km from the nearest OPW station the depth prediction
  should be treated as indicative only
- River distance uses OPW station proximity — accurate for major rivers,
  may underestimate proximity to smaller unmonitored streams
- Navigation sidebar collapses to hamburger on mobile — a dedicated top
  navigation bar is planned for a future version

---

## Future Enhancements

- Real-time rainfall API integration
- Live flood spread calculation based on rainfall input in mm over given hours
- Safe route navigation by foot and by road during flood events
- UK and East Africa coverage
- Land use suitability analysis — data centre placement, crop suitability,
  solar and wind farm site selection
- OPW flood zone boundary overlay on predictor map using verified WMS endpoint
- Real-time flood alerts when OPW water levels exceed threshold in a given area
- Turlough and seasonal flood plain mapping using OPW CFRAM dataset
- Known flood-prone road sections overlay using historical OPW past flood data
- Full Irish river network dataset to improve river distance accuracy
- Dedicated top navigation bar for mobile users
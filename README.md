# FloodSave — Flood Risk Prediction System

## Overview
FloodSave is an intelligent flood risk prediction platform that classifies 
flood risk and predicts flood depth for any Irish location using geographic 
and environmental data. Built on real-time OPW hydrometric station data 
with a scalable architecture designed for future global expansion.

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

## Current Coverage
- Ireland (active) — OPW hydrometric station network

---

## Dataset Content

The dataset is sourced from the Irish Office of Public Works (OPW) 
Real-Time Water Levels API at waterlevel.ie/geojson — a live endpoint 
updated continuously by OPW hydrometric data loggers across Ireland.

**Data freshness:** The OPW API provides real-time readings. The station 
list was pulled on April 2026 and contains 457 active monitoring stations. 
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
| distance_to_river_m | Estimated distance to nearest river |
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
- **Learning method:** Supervised classification using Random Forest
- **Ideal outcome:** Model correctly classifies flood risk with at least 
  75% accuracy on unseen test data
- **Success metric:** Accuracy score above 0.75, F1 score above 0.70
- **Failure metric:** Accuracy below 0.75 — model not deployed
- **Model output:** Risk category label displayed on dashboard predictor page
- **Training data:** OPW flood zone data with engineered features

### Regression Task
- **Aim:** Predict expected flood depth in metres for a given location
- **Learning method:** Supervised regression using Random Forest Regressor
- **Ideal outcome:** Model predicts flood depth within acceptable margin
- **Success metric:** R2 score above 0.75 on test set
- **Failure metric:** R2 below 0.75 — model performance noted on dashboard
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
  R2 score, Actual vs Predicted plot and feature importance. Answers BR2 and BR3.

---

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

## Future Enhancements

- Real-time rainfall API integration
- Live flood spread calculation
- Safe route navigation by foot
- Safe route navigation by road
- UK and East Africa coverage
- Land use suitability analysis — data centre placement, 
  crop suitability, solar and wind farm site selection 
  using flood risk combined with sunshine hours, 
  rainfall and soil type data
- Reverse geocoding to show nearest town for each station
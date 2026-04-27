# FloodSave — Flood Risk Prediction System

**Author:** Damaris Alum
**GitHub:** [Alumsdesigns](https://github.com/Alumsdesigns)
**Email:** alum.damaris@gmail.com
**View the Floodsave Web Application:** [View Deployed Site](https://floodsave-bf0f49c3b6af.herokuapp.com/) 


Enjoy learning more about flood risks in different areas

---

## Table of Contents

1. [Overview](#overview)
2. [Value and Impact](#value-and-impact)
3. [CRISP-DM Process](#crisp-dm-process)
4. [UX Design Decisions](#ux-design-decisions)
5. [File Structure](#file-structure)
6. [Project Documentation](#project-documentation)
7. [Dataset Content](#dataset-content)
8. [Business Requirements](#business-requirements)
9. [User Stories](#user-stories)
10. [User Story to ML Task Mapping](#user-story-to-ml-task-mapping)
11. [Hypotheses and Validation Results](#hypotheses-and-validation-results)
12. [ML Business Case](#ml-business-case)
13. [Rationale to Map Business Requirements to ML Tasks](#rationale-to-map-business-requirements-to-ml-tasks)
14. [Dashboard Design](#dashboard-design)
15. [Saved Plot Outputs](#saved-plot-outputs)
16. [Testing and Iteration](#testing-and-iteration)
17. [Tech Stack](#tech-stack)
18. [Deployment](#deployment)
19. [Main Data Analysis and Machine Learning Libraries](#main-data-analysis-and-machine-learning-libraries)
20. [Bug Fixes](#bug-fixes)
21. [Unfixed Bugs](#unfixed-bugs)
22. [Future Enhancements](#future-enhancements)
23. [Credits](#credits)
24. [Note for Assessors](#note-for-assessors)
25. [License](#license)

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
| Deployment | Heroku — https://floodsave-bf0f49c3b6af.herokuapp.com |

---

## UX Design Decisions

The dashboard follows these UX principles:

- **Information hierarchy:** Summary page first, predictor last — users understand context before making predictions
- **Consistency:** Same card components, colour scheme and layout pattern across all 5 pages via shared src/styles.py
- **User feedback:** Status messages and spinners confirm every action is processing — users are never left waiting without feedback
- **Accessibility:** Colour contrast meets WCAG AA standard (minimum 4.5:1 ratio). All charts include text labels and hover tooltips for screen reader compatibility
- **Mobile responsive:** Single column layout on screens below 1024px. Sidebar collapses to hamburger menu on mobile
- **User control:** No auto-playing content. All predictions triggered
  by explicit user action
- **Colour palette:** Dark navy `#1a1a2e` for headings, primary blue `#4a90d9`for interactive elements and section underlines, white `#ffffff` for card backgrounds. Risk levels use semantic colours — red `#c0392b` for High, amber `#d35400` for Medium, green `#1e8449` for Low. All colours meet WCAG AA contrast standard
- **Typography:** Two font pairing — Plus Jakarta Sans (Google Fonts) for headings and display values, DM Sans (Google Fonts) for body text and UI labels. Six level typographic scale: H1 page titles at 2.2rem/800 weight, H2 section headers at 1.15rem/600 weight, display card values at 1.75rem/700 weight, card labels at 0.70rem/600 uppercase, body text at 0.90rem/400, subtitles at 0.78rem/400. All levels have explicit line-height and letter-spacing defined
- **Component library:** Shared reusable components in src/styles.py — metric cards, info boxes, result boxes, risk badges, section headers and back to top button. All built with BEM CSS naming convention
- **User control:** No auto-playing content. All predictions triggered by explicit user action. Empty form submission returns a clear warning message rather than silently failing, all interactions produce visible feedback

---

## File Structure

```
floodsave/
├── app_pages
│   ├── __init__.py
│   ├── page_flood_risk_study.py
│   ├── page_hypothesis_validation.py
│   ├── page_model_performance.py
│   ├── page_risk_predictor.py
│   └── page_summary.py
├── docs
│   ├── crisp_dm.md
│   ├── hypothesis_validation.md
│   ├── ml_pipeline.md
│   └── user_flow.md
├── inputs
│   └── datasets
│       └── raw
│           └── ireland_flood_data.csv
├── jupyter_notebooks
│   ├── 01_data_collection.ipynb
│   ├── 02_data_cleaning.ipynb
│   ├── 03_feature_engineering.ipynb
│   ├── 04_data_visualisation.ipynb
│   ├── 05_hypothesis_validation.ipynb
│   ├── 06_modeling_classification.ipynb
│   └── 07_modeling_regression.ipynb
├── outputs
│   └── v1
│       ├── plots
│       │   ├── 01_elevation_histogram.png
│       │   ├── 02_elevation_vs_depth_scatter.png
│       │   ├── 03_correlation_heatmap.png
│       │   ├── 04_flood_depth_boxplot.png
│       │   ├── 05_feature_importance.png
│       │   └── 06_actual_vs_predicted.png
│       ├── classification_pipeline.pkl
│       ├── cleaned_data.csv
│       ├── featured_data.csv
│       └── regression_pipeline.pkl
├── src
│   ├── __init__.py 
│   ├── data_management.py
│   ├── ml_pipeline.py
│   └── styles.py
├── app.py
├── Procfile
├── README.md
├── requirements.txt
├── runtime.txt
└── setup.sh
```

---

## Project Documentation

Additional technical documentation is available in the `docs/` folder:

| File | Contents |
|------|----------|
| [crisp_dm.md](docs/crisp_dm.md) | CRISP-DM phase breakdown with tasks completed at each stage |
| [hypothesis_validation.md](docs/hypothesis_validation.md) | Detailed statistical test outputs and interpretation |
| [ml_pipeline.md](docs/ml_pipeline.md) | ML pipeline architecture, feature engineering and model selection rationale |
| [user_flow.md](docs/user_flow.md) | User journey diagrams for each stakeholder type |

---

## Dataset Content

The dataset is sourced from the Irish Office of Public Works (OPW)
Real-Time Water Levels API at waterlevel.ie/geojson — a live endpoint
updated continuously by OPW hydrometric data loggers across Ireland.

**Data freshness:** The OPW API provides real-time readings. The station
list was pulled in April 2026 and contains 457 active monitoring stations.
Each station transmits water level data via GPRS telemetry at regular
intervals. The dataset is licensed under Creative Commons CC-BY 4.0.

**Ethics and Privacy:** The OPW dataset is published under Creative Commons 
CC-BY 4.0 licence. It is publicly available and contains no personal data. 
No anonymisation was required.

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

### Saved Plot Outputs

All dashboard visualisations are generated dynamically using Plotly. 
Static versions of each plot are saved to `outputs/v1/plots/` during 
notebook execution for reference:

| File | Plot | Dashboard Page |
|------|------|---------------|
| 01_elevation_histogram.png | Elevation distribution histogram | Flood Risk Study |
| 02_elevation_vs_depth_scatter.png | Elevation vs flood depth scatter | Flood Risk Study |
| 03_correlation_heatmap.png | Feature correlation heatmap | Flood Risk Study |
| 04_flood_depth_boxplot.png | Flood depth by risk category boxplot | Flood Risk Study |
| 05_feature_importance.png | Random Forest feature importance | Model Performance |
| 06_actual_vs_predicted.png | Actual vs predicted flood depth | Model Performance |

---

## Testing and Iteration

### Manual Testing

The dashboard was tested manually across all five pages during development.
Each feature was verified to work as expected before being committed.

| Test | Expected | Result |
|------|----------|--------|
| Location search returns result | Prediction displays below map | Pass |
| Map click triggers prediction | Results update automatically | Pass |
| Search outside Ireland rejected | Warning message displayed | Pass |
| Back to top button scrolls page | Returns to page anchor | Pass |
| Sidebar collapses on mobile | Hamburger menu appears | Pass |
| All 5 pages load without error | Content renders correctly | Pass |
| Model loads pkl files correctly | No import errors on startup | Pass |
| Empty search form submitted | Warning message displayed | Pass |

### End User Testing

The dashboard was tested with three end users representing the target
audience — a construction professional, an insurance professional and
a member of the public with no technical background.

**Feedback received and acted on:**

| Feedback | Action Taken |
|----------|-------------|
| Plain English explanation needed for each chart | Added info_box text above every plot explaining what the chart shows and how to read it |
| Results were not visible after clicking the map | Moved prediction results outside the two-column layout so they span full width |
| Location input was not clearing after a map click | Replaced st.text_input with st.form using clear_on_submit=True |
| Clicking the same area repeatedly caused freezing | Added click_key tracking at 4dp precision to detect only new clicks |
| P-value explanation was unclear | Added plain English p-value definition at top of Hypothesis Validation page |

### Browser Testing

| Browser | Result |
|---------|--------|
| Chrome | Pass |
| Firefox | Pass |
| Safari | Pass |
| Mobile Chrome | Pass |

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
| Deployment | Heroku | Cloud platform for live deployment |

---

## Deployment

The application is deployed on Heroku.

**Live Site:** https://floodsave-bf0f49c3b6af.herokuapp.com

### Deployment Steps
1. Created Heroku app via Heroku dashboard
2. Connected GitHub repository Alumsdesigns/floodsave
3. Deployed from main branch
4. Heroku-24 stack with Python 3.13
5. All deployment files maintained in repo — Procfile, runtime.txt, setup.sh

### Local Development
```bash
git clone git@github.com:Alumsdesigns/floodsave.git
cd floodsave
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
streamlit run app.py
```

---

## Main Data Analysis and Machine Learning Libraries

| Library | Purpose | Example Usage |
|---------|---------|---------------|
| streamlit | Interactive dashboard interface | st.plotly_chart() renders interactive charts |
| scikit-learn | Random Forest models, GridSearchCV | RandomForestClassifier with GridSearchCV — 486 combinations |
| matplotlib | Static charts in notebooks | plt.savefig() saves plots to outputs/v1/plots/ |
| seaborn | Statistical visualisations | sns.heatmap() for correlation matrix in notebooks |
| plotly | Interactive charts on dashboard | px.histogram() for elevation distribution chart |
| scipy | Statistical tests | chi2_contingency() for hypothesis 1 chi-square test |
| folium | Interactive map | folium.Map() with click-to-predict on Risk Predictor page |
| streamlit-folium | Renders Folium map inside Streamlit | st_folium() returns last_clicked coordinates |
| geopy | Geocodes location names | Nominatim().geocode() converts town name to lat/lng |
| joblib | Saves and loads ML pipelines | joblib.load() reads classification_pipeline.pkl |
| pandas | Data manipulation | pd.read_csv() loads featured_data.csv for EDA |
| numpy | Numerical computation | np.array() used in haversine distance calculation |

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
| Search form submitted with empty input gave no feedback | Added st.warning message when form submitted without location input |

---

## Unfixed Bugs

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

---

## Credits

- OPW Real-Time Water Levels API — waterlevel.ie — CC-BY 4.0 licence
- Open-Elevation API — open-elevation.com — open source elevation data
- Code Institute walkthrough projects — Churnometer and Heritage Housing 
  Issues — used as inspiration for CRISP-DM structure and README format
- Streamlit documentation — docs.streamlit.io
- Scikit-learn documentation — scikit-learn.org
- Folium documentation — python-visualization.github.io/folium

---

## Note for Assessors

This project demonstrates:

- **LO1-LO7** — All learning outcomes addressed across notebooks, dashboard and README
- **CRISP-DM compliance** — All 6 phases documented and implemented
- **Original dataset** — Live OPW API data, not a Kaggle dataset
- **Two ML pipelines** — Classification (100% accuracy) and Regression (R2=0.59)
- **Distinction criteria** — 3 hypotheses validated, 6+ hyperparameters tuned,
  4 plot types, professional UI, comments in all code files
- **Deployment** — Live on Heroku at https://floodsave-bf0f49c3b6af.herokuapp.com
- **Author:** Damaris Alum - Code Institute Predictive Analytics Portfolio Project 5

---

## License

Educational project for Code Institute Portfolio Project 5 — Predictive Analytics.



# CRISP-DM Process
## What this is
CRISP-DM (Cross Industry Standard Process for Data Mining) is the 
6-step framework used to structure this project. Each phase maps 
directly to one or more Jupyter notebooks in this project.

## Why it matters
Criteria 1.1 requires evidence that the project follows the 
Business Understanding phase of CRISP-DM by describing the dataset 
and business requirements. This diagram shows the full process 
and proves deliberate methodology was followed from data collection 
through to deployment.

```mermaid
flowchart LR
    classDef phase fill:#1A237E,color:#fff,stroke:#0D1450

    B["Business Understanding
    ─────────────
    Who needs flood risk?
    Construction, insurance,
    councils, public safety
    README Business Case"]:::phase

    D["Data Understanding
    ─────────────
    Notebook 01
    Notebook 04
    EDA + visualisation"]:::phase

    P["Data Preparation
    ─────────────
    Notebook 02
    Notebook 03
    Clean + engineer"]:::phase

    M["Modelling
    ─────────────
    Notebook 06
    Notebook 07
    RF + GridSearchCV"]:::phase

    E["Evaluation
    ─────────────
    R2 score
    Confusion matrix
    Hypothesis tests"]:::phase

    DEP["Deployment
    ─────────────
    Streamlit
    Community Cloud
    Public URL"]:::phase

    B --> D --> P --> M --> E --> DEP
    DEP -.->|"iterate on new data"| B
```

## College criteria covered
- 1.1 CRISP-DM compliance 
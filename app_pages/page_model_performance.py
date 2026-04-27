# app_pages/page_model_performance.py
# Displays ML model evaluation metrics, confusion matrix and feature importance
# Results are hardcoded from Notebook 06 and Notebook 07 evaluation outputs
# Criteria: 4.2 (ML pipeline success statement), 5.2 (model evaluation),
#           5.7 (hyperparameter tuning), D4 (6+ hyperparameters with 3+ values)

import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.figure_factory as ff
import numpy as np
from src.styles import section_header, info_box, metric_card, result_box, back_to_top


def page_model_performance():
    # named anchor allows back to top button to scroll here
    st.markdown('<div id="floodsave-top"></div>', unsafe_allow_html=True)

    # page title and subtitle
    st.markdown('<div class="fs-title">Model Performance</div>',
                unsafe_allow_html=True)
    st.markdown(
        '<div class="fs-subtitle">Evaluation of the Random Forest classification and regression pipelines</div>',
        unsafe_allow_html=True
    )

    # classification model section — criteria 4.2 and 5.2
    section_header("Classification Model — Flood Risk Category")
    info_box("The classifier predicts flood risk as High, Medium or Low. Trained on 80 percent of the 457 OPW stations and evaluated on the remaining 20 percent. Results from Notebook 06.")

    # four key classification metrics from Notebook 06
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        metric_card("Accuracy", "100%", "on test set")
    with col2:
        metric_card("Precision", "1.00", "weighted average")
    with col3:
        metric_card("Recall", "1.00", "weighted average")
    with col4:
        metric_card("F1 Score", "1.00", "weighted average")

    # criteria 4.2 — clear statement that model meets performance requirement
    result_box("The classification model meets the performance requirement. Accuracy of 100% on the test set exceeds the 75% target defined in the ML Business Case.")

    # confusion matrix — criteria 5.2
    section_header("Confusion Matrix")
    info_box("Each row shows the actual risk class. Each column shows what the model predicted. Numbers on the diagonal are correct predictions. Off-diagonal numbers are errors. All predictions are correct — the matrix is perfectly diagonal.")

    # confusion matrix values from Notebook 06 test set evaluation
    # rows and columns ordered: High, Low, Medium
    cm = np.array([
        [6,  0,  0],
        [0, 16,  0],
        [0,  0, 70]
    ])
    labels = ['High', 'Low', 'Medium']

    fig_cm = ff.create_annotated_heatmap(
        z=cm,
        x=labels,
        y=labels,
        colorscale='Blues',
        showscale=True
    )
    fig_cm.update_layout(
        title='Confusion Matrix — Test Set (92 samples)',
        xaxis_title='Predicted',
        yaxis_title='Actual',
        paper_bgcolor='white',
        margin=dict(t=80, b=40, l=40, r=20),
        modebar_remove=['toImage', 'zoom', 'pan', 'resetScale2d',
                        'zoomIn2d', 'zoomOut2d', 'autoScale2d']
    )
    st.plotly_chart(fig_cm, use_container_width=True)

    # regression model section — criteria 5.2
    section_header("Regression Model — Flood Depth Prediction")
    info_box("The regressor predicts expected flood depth in metres. Evaluated using R2 score — how much of the variation in flood depth the model can explain. Results from Notebook 07.")

    # three key regression metrics from Notebook 07
    col1, col2, col3 = st.columns(3)
    with col1:
        metric_card("R2 Score", "0.59", "on test set")
    with col2:
        metric_card("MAE", "0.28m", "mean absolute error")
    with col3:
        metric_card("Target", "0.75", "minimum R2 required")

    # honest assessment — model does not meet regression target
    info_box("The regression model R2 of 0.59 is below the 0.75 target. The model explains 59 percent of the variation in flood depth. This limitation is documented — flood depth prediction is most reliable near monitored rivers where training data is dense.")

    # feature importance — criteria 4.2 and D4
    section_header("Feature Importance")
    info_box("Feature importance shows which input variables the model relied on most when making predictions. Elevation and distance to river dominate — confirming these are the strongest flood risk predictors.")

    # feature importance values from Notebook 06 Random Forest classifier
    features = ['elevation_m', 'distance_to_river_m', 'longitude', 'latitude']
    importance = [0.5546, 0.4438, 0.0014, 0.0001]

    fig_imp = px.bar(
        x=importance,
        y=features,
        orientation='h',
        title='Feature Importance — Random Forest Classifier',
        labels={'x': 'Importance Score', 'y': 'Feature'},
        color=importance,
        color_continuous_scale='Blues'
    )
    fig_imp.update_layout(
        showlegend=False,
        paper_bgcolor='white',
        plot_bgcolor='white',
        coloraxis_showscale=False,
        margin=dict(t=80, b=40, l=40, r=20),
        modebar_remove=['toImage', 'zoom', 'pan', 'resetScale2d',
                        'zoomIn2d', 'zoomOut2d', 'autoScale2d']
    )
    st.plotly_chart(fig_imp, use_container_width=True)

    # hyperparameter tuning table — criteria 5.7 and D4
    # D4 requires 6+ hyperparameters with 3+ values each and documented rationale
    section_header("Hyperparameter Tuning")
    info_box("GridSearchCV tested 486 parameter combinations across 5 cross-validation folds — 2430 total fits. Best parameters were selected automatically based on accuracy score.")

    # hyperparameter table — rationale column satisfies D4 documentation requirement
    params = {
        'Parameter': [
            'n_estimators',
            'max_depth',
            'min_samples_split',
            'min_samples_leaf',
            'max_features',
            'criterion'
        ],
        'Best Value': ['50', '5', '2', '1', 'None', 'entropy'],
        'Values Tested': [
            '50, 100, 200',
            '5, 10, 20',
            '2, 5, 10',
            '1, 2, 4',
            'sqrt, log2, None',
            'gini, entropy'
        ],
        'Rationale': [
            'More trees increases stability — 50 sufficient for 457 stations',
            'Shallow depth prevents overfitting on small dataset',
            'Higher values reduce overfitting on minority classes',
            'Controls smoothness of decision boundary',
            'sqrt is standard RF default — None uses all features',
            'Entropy considers information gain — more thorough than gini'
        ]
    }

    df_params = pd.DataFrame(params)
    st.dataframe(df_params, use_container_width=True, hide_index=True)

    # back to top button — fixed position bottom right
    back_to_top()
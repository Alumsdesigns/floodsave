# Purpose: EDA page with 4 interactive Plotly charts answering BR1
# Criteria: 3.1, 6.2, 6.4, 6.5, D5

import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
from src.styles import section_header, info_box
from src.data_management import load_featured_data


def page_flood_risk_study():
    st.markdown('<div class="fs-title">Flood Risk Study</div>',
                unsafe_allow_html=True)
    st.markdown('<div class="fs-subtitle">Exploratory analysis of Irish flood risk patterns across 457 OPW stations</div>',
                unsafe_allow_html=True)

    df = load_featured_data()

    # Plot 1 — Histogram
    section_header("Plot 1 — Elevation Distribution")
    info_box("""
        What this shows: A count of how many OPW monitoring stations
        sit at each elevation band. The taller the bar, the more stations
        at that height. Count means the number of stations in that
        elevation range — for example count=12 means 12 stations have
        elevation between those two values. The red line is the average
        elevation of 203 metres. Stations to the RIGHT of the red line
        are above average elevation and are generally safer from flooding.
        Stations to the LEFT are below average and are more likely to be
        in flood-prone lowland areas. Hover over any bar to see the exact
        count and elevation range.
    """)
    fig1 = px.histogram(
        df, x='elevation_m', nbins=30,
        title='Distribution of Elevation Across Irish Flood Monitoring Stations',
        labels={'elevation_m': 'Elevation (metres)', 'count': 'Number of Stations'},
        color_discrete_sequence=['#4a90d9']
    )
    fig1.add_vline(
        x=df['elevation_m'].mean(),
        line_dash='dash', line_color='red',
        annotation_text=f"Mean: {df['elevation_m'].mean():.0f}m",
        annotation_position='top right'
    )
    fig1.update_layout(
        showlegend=False,
        plot_bgcolor='white',
        paper_bgcolor='white',
        margin=dict(t=50, b=40, l=40, r=20)
    )
    st.plotly_chart(fig1, use_container_width=True)

    # Plot 2 — Scatter
    section_header("Plot 2 — Elevation vs Flood Depth")
    info_box("""
        What this shows: Each dot is one OPW monitoring station.
        LEFT = low elevation, RIGHT = high elevation.
        TOP = deeper flooding, BOTTOM = shallower flooding.
        Red dots are High risk — they cluster at low elevation
        with deep floods. Green dots are Low risk — high elevation,
        shallow floods. Hover over any dot to see the station name,
        exact elevation and flood depth.
    """)
    color_map = {'High': '#e74c3c', 'Medium': '#f39c12', 'Low': '#2ecc71'}
    fig2 = px.scatter(
        df, x='elevation_m', y='flood_depth_m',
        color='flood_risk',
        color_discrete_map=color_map,
        hover_name='name',
        hover_data={
            'elevation_m': ':.1f',
            'flood_depth_m': ':.2f',
            'flood_risk': True,
            'region': True,
            'distance_to_river_m': ':.1f',
            'latitude': ':.4f',
            'longitude': ':.4f'
        },
        title='Elevation vs Flood Depth by Risk Category',
        labels={
            'elevation_m': 'Elevation (metres)',
            'flood_depth_m': 'Flood Depth (metres)',
            'flood_risk': 'Risk Category',
            'region': 'Region (West / Midlands / East)',
            'distance_to_river_m': 'Distance to River (m)'
        }
    )
    fig2.update_traces(marker=dict(size=7, opacity=0.7))
    fig2.update_layout(
        plot_bgcolor='white',
        paper_bgcolor='white',
        margin=dict(t=50, b=40, l=40, r=20)
    )
    st.plotly_chart(fig2, use_container_width=True)

    # Plot 3 — Heatmap
    section_header("Plot 3 — Correlation Heatmap")
    info_box("""
        What this shows: Each square answers — when one measurement
        increases, what happens to the other? Numbers range from
        -1 to +1. BLUE (negative) means opposite movement — elevation
        vs flood risk is -0.58, meaning higher ground means lower risk.
        RED (positive) means same direction — flood depth vs flood risk
        is +0.79, meaning deeper floods always mean higher risk.
        The stronger the colour, the stronger the relationship.
        Hover over any square to see the exact value.
    """)
    numeric_cols = ['elevation_m', 'distance_to_river_m',
                    'flood_depth_m', 'flood_risk_encoded']
    corr = df[numeric_cols].corr().round(2)
    fig3 = px.imshow(
        corr,
        text_auto=True,
        color_continuous_scale='RdBu_r',
        zmin=-1, zmax=1,
        title='Correlation Matrix — Flood Risk Features',
        labels=dict(color='Correlation')
    )
    fig3.update_layout(
        margin=dict(t=50, b=40, l=40, r=20),
        paper_bgcolor='white'
    )
    st.plotly_chart(fig3, use_container_width=True)

    # Plot 4 — Boxplot
    section_header("Plot 4 — Flood Depth by Risk Category")
    info_box("""
        What this shows: The spread of flood depth within each risk
        group. The LINE inside each box is the median depth — half
        the stations are above it, half below. The BOX edges show
        where the middle 50 percent of stations sit. The LINES
        extending out show the full range. Green (Low risk) sits
        near zero. Orange (Medium) sits around 0.5 to 1.5 metres.
        Red (High risk) sits between 1.5 and 3 metres. Hover over
        any box to see exact statistics. Clear separation between
        groups confirms the model correctly identifies risk levels.
    """)
    fig4 = px.box(
        df, x='flood_risk', y='flood_depth_m',
        color='flood_risk',
        color_discrete_map=color_map,
        category_orders={'flood_risk': ['Low', 'Medium', 'High']},
        hover_data=['name', 'region'],
        title='Flood Depth Distribution by Risk Category',
        labels={
            'flood_risk': 'Flood Risk Category',
            'flood_depth_m': 'Flood Depth (metres)'
        }
    )
    fig4.update_layout(
        showlegend=False,
        plot_bgcolor='white',
        paper_bgcolor='white',
        margin=dict(t=50, b=40, l=40, r=20)
    )
    st.plotly_chart(fig4, use_container_width=True)

    section_header("Key Conclusions")
    col1, col2 = st.columns(2)
    with col1:
        info_box("Elevation is the strongest single predictor — lower ground means higher risk.")
        info_box("Distance to river is the second strongest predictor — within 100m significantly increases risk.")
    with col2:
        info_box("Western stations show higher flood depth than Eastern stations due to Atlantic rainfall.")
        info_box("All four plots together answer BR1 — geographic features correlate strongly with flood risk.")

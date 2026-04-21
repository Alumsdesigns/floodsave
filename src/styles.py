# Purpose: Shared CSS and reusable UI components for all dashboard pages
# Import apply_custom_css() in app.py once — all pages inherit styles

import streamlit as st

def apply_custom_css():
    st.markdown("""
    <style>
    /* Global */
    .main .block-container {
        padding-top: 0.5rem;
        padding-bottom: 1.5rem;
        max-width: 1100px;
    }

    .block-container {
    padding-top: 0.5rem !important;
    }

    /* Hide default Streamlit header */
    header[data-testid="stHeader"] {
        background: transparent;
    }

    /* Page title */
    .fs-title {
        font-size: 1.8rem;
        font-weight: 700;
        color: #1a1a2e;
        margin: 0rem;
    }

    .fs-subtitle {
        font-size: 1rem;
        color: #666;
        margin-bottom: .5rem;
    }

    /* Divider */
    .fs-divider {
        border: none;
        border-top: 1px solid #e0e0e0;
        margin: 1.2rem 0;
    }

    /* Metric card */
    .fs-card {
        background: #ffffff;
        border: 1px solid #e8e8e8;
        border-radius: 12px;
        padding: 1.2rem 1.4rem;
        text-align: center;
        box-shadow: 0 2px 8px rgba(0,0,0,0.06);
        height: 100%;
    }

    .fs-card-label {
        font-size: 0.78rem;
        font-weight: 600;
        color: #555;
        text-transform: uppercase;
        letter-spacing: 0.05em;
        margin-bottom: 0.4rem;
    }

    .fs-card-value {
        font-size: 1.9rem;
        font-weight: 700;
        color: #1a1a2e;
        line-height: 1.2;
    }

    .fs-card-sub {
        font-size: 0.8rem;
        color: #444;
        margin-top: 0.3rem;
        font-weight: 400;
    }

    /* Risk badge */
    .fs-badge-high {
        background: #ffe5e5;
        color: #c0392b;
        border: 1px solid #f5b7b1;
        border-radius: 20px;
        padding: 0.3rem 0.9rem;
        font-size: 0.85rem;
        font-weight: 600;
        display: inline-block;
    }

    .fs-badge-medium {
        background: #fff3e0;
        color: #e67e22;
        border: 1px solid #fad7a0;
        border-radius: 20px;
        padding: 0.3rem 0.9rem;
        font-size: 0.85rem;
        font-weight: 600;
        display: inline-block;
    }

    .fs-badge-low {
        background: #e8f8f5;
        color: #1e8449;
        border: 1px solid #a9dfbf;
        border-radius: 20px;
        padding: 0.3rem 0.9rem;
        font-size: 0.85rem;
        font-weight: 600;
        display: inline-block;
    }

    /* Section header */
    .fs-section {
        font-size: 1.1rem;
        font-weight: 600;
        color: #1a1a2e;
        margin-top: 1rem;
        margin-bottom: 0.4rem;
        padding-bottom: 0.3rem;
        border-bottom: 2px solid #4a90d9;
        display: inline-block;
        width: auto;
    }

    /* Info box */
    .fs-info {
        background: #f0f7ff;
        border-left: 4px solid #4a90d9;
        border-radius: 0 8px 8px 0;
        padding: 0.8rem 1rem;
        font-size: 0.9rem;
        color: #333;
        margin: 0.8rem 0;
    }

    /* Result box */
    .fs-result {
        background: #f8fff8;
        border: 1px solid #a9dfbf;
        border-radius: 12px;
        padding: 1.2rem;
        text-align: center;
        margin: 1rem 0;
    }

    /* Responsive — mobile */
    @media (max-width: 768px) {
        .fs-title { font-size: 1.4rem; }
        .fs-card-value { font-size: 1.5rem; }
        .main .block-container {
            padding-left: 1rem;
            padding-right: 1rem;
        }
    }
    </style>
    """, unsafe_allow_html=True)


def metric_card(label, value, sub=None):
    """Reusable metric card component"""
    sub_html = f'<div class="fs-card-sub">{sub}</div>' if sub else ''
    st.markdown(f"""
    <div class="fs-card">
        <div class="fs-card-label">{label}</div>
        <div class="fs-card-value">{value}</div>
        {sub_html}
    </div>
    """, unsafe_allow_html=True)


def risk_badge(risk):
    """Color coded risk badge — High, Medium or Low"""
    css_class = f"fs-badge-{risk.lower()}"
    st.markdown(f'<span class="{css_class}">{risk} Risk</span>',
                unsafe_allow_html=True)


def section_header(text):
    """Consistent section header with blue underline"""
    st.markdown(f'<div class="fs-section">{text}</div>',
                unsafe_allow_html=True)


def info_box(text):
    """Styled info box with left blue border"""
    st.markdown(f'<div class="fs-info">{text}</div>',
                unsafe_allow_html=True)


def result_box(html_content):
    """Styled result box for predictions"""
    st.markdown(f'<div class="fs-result">{html_content}</div>',
                unsafe_allow_html=True)
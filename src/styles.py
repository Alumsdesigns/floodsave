# Purpose: Shared CSS and reusable UI components for all dashboard pages
# Call apply_custom_css() once in app.py — all pages inherit styles

import streamlit as st


def apply_custom_css():
    st.markdown("""
    <style>
    /* ── Layout ── */
    .appview-container .main .block-container {
            padding-top: 1rem;
            padding-bottom: 2rem;
            padding-left: 2rem;
            padding-right: 2rem;
            max-width: 1100px;
    }

    /* ── Sidebar ── */
    section[data-testid="stSidebar"] {
        min-width: 220px;
        max-width: 260px;
    }

    section[data-testid="stSidebar"] .fs-title {
        font-size: 1.2rem;
    }

    /* ── Typography ── */
    .fs-title {
        font-size: 1.8rem;
        font-weight: 700;
        color: #1a1a2e;
        margin: 0;
        line-height: 1.2;
    }

    .fs-subtitle {
        font-size: 0.95rem;
        color: #555;
        margin: 0.2rem 0 0.8rem 0;
    }

    /* ── Section header ── */
    .fs-section {
        font-size: 1.05rem;
        font-weight: 600;
        color: #1a1a2e;
        margin: 1rem 0 0.4rem 0;
        padding-bottom: 0.25rem;
        border-bottom: 2px solid #4a90d9;
        display: inline-block;
    }

    /* ── Cards ── */
    .fs-card {
        background: #ffffff;
        border: 1px solid #e2e2e2;
        border-radius: 10px;
        padding: 1rem 1.2rem;
        text-align: center;
        box-shadow: 0 1px 4px rgba(0, 0, 0, 0.05);
        margin: 0.3rem 0;
    }

    .fs-card-label {
        font-size: 0.72rem;
        font-weight: 600;
        color: #555;
        text-transform: uppercase;
        letter-spacing: 0.06em;
        margin-bottom: 0.3rem;
    }

    .fs-card-value {
        font-size: 1.7rem;
        font-weight: 700;
        color: #1a1a2e;
        line-height: 1.2;
    }

    .fs-card-sub {
        font-size: 0.8rem;
        color: #444;
        margin-top: 0.25rem;
    }

    /* ── Info box ── */
    .fs-info {
        background: #f0f7ff;
        border-left: 3px solid #4a90d9;
        border-radius: 0 6px 6px 0;
        padding: 0.7rem 1rem;
        font-size: 0.88rem;
        color: #333;
        margin: 0.5rem 0;
        line-height: 1.5;
    }

    /* ── Result box ── */
    .fs-result {
        background: #f6fff6;
        border: 1px solid #a9dfbf;
        border-radius: 10px;
        padding: 1.2rem;
        text-align: center;
        margin: 0.8rem 0;
    }

    /* ── Risk badges ── */
    .fs-badge-high {
        background: #ffe5e5;
        color: #c0392b;
        border: 1px solid #f5b7b1;
        border-radius: 20px;
        padding: 0.25rem 0.8rem;
        font-size: 0.85rem;
        font-weight: 600;
        display: inline-block;
    }

    .fs-badge-medium {
        background: #fff3e0;
        color: #d35400;
        border: 1px solid #fad7a0;
        border-radius: 20px;
        padding: 0.25rem 0.8rem;
        font-size: 0.85rem;
        font-weight: 600;
        display: inline-block;
    }

    .fs-badge-low {
        background: #e8f8f5;
        color: #1e8449;
        border: 1px solid #a9dfbf;
        border-radius: 20px;
        padding: 0.25rem 0.8rem;
        font-size: 0.85rem;
        font-weight: 600;
        display: inline-block;
    }

    /* ── Column spacing ── */
    .fs-col-gap > div[data-testid="column"] {
        padding-left: 0.4rem;
        padding-right: 0.4rem;
    }

    /* ── Mobile ── */
    @media screen and (max-width: 768px) {
    
        .appview-container .main .block-container {
            padding-top: 2.5rem;
            padding-left: 1rem;
            padding-right: 1rem;
        }

        .fs-title {
            font-size: 1.3rem;
        }

        .fs-card-value {
            font-size: 1.4rem;
        }

        .fs-card {
            margin-bottom: 0.5rem;
        }
    }

    /* ── Hide default sidebar arrow and replace with hamburger ── */
    button[data-testid="baseButton-headerNoPadding"] {
        display: none;
    }

    [data-testid="collapsedControl"] {
        display: flex;
        align-items: center;
        justify-content: center;
        width: 2.2rem;
        height: 2.2rem;
        background: #1a1a2e;
        border-radius: 6px;
        cursor: pointer;
        top: 0.6rem;
        left: 0.6rem;
        position: fixed;
        z-index: 999;
    }

    [data-testid="collapsedControl"]::before {
        content: "";
        display: block;
        width: 16px;
        height: 2px;
        background: #ffffff;
        box-shadow: 0 5px 0 #ffffff, 0 10px 0 #ffffff;
    }


    </style>
    """, unsafe_allow_html=True)


def metric_card(label, value, sub=None):
    """Reusable metric card — label, large value, optional subtitle"""
    sub_html = f'<div class="fs-card-sub">{sub}</div>' if sub else ''
    st.markdown(f"""
    <div class="fs-card">
        <div class="fs-card-label">{label}</div>
        <div class="fs-card-value">{value}</div>
        {sub_html}
    </div>
    """, unsafe_allow_html=True)


def risk_badge(risk):
    """Color coded risk badge — pass High, Medium or Low"""
    css_class = f"fs-badge-{risk.lower()}"
    st.markdown(
        f'<span class="{css_class}">{risk} Risk</span>',
        unsafe_allow_html=True
    )


def section_header(text):
    """Section header with blue underline — width matches text"""
    st.markdown(
        f'<div class="fs-section">{text}</div>',
        unsafe_allow_html=True
    )


def info_box(text):
    """Info box with left blue border"""
    st.markdown(
        f'<div class="fs-info">{text}</div>',
        unsafe_allow_html=True
    )


def result_box(html_content):
    """Green tinted result box for prediction output"""
    st.markdown(
        f'<div class="fs-result">{html_content}</div>',
        unsafe_allow_html=True
    )

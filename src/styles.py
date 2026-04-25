# src/styles.py
# Purpose: Shared CSS and reusable UI components for all dashboard pages
# Call apply_custom_css() once in app.py — all pages inherit styles

import streamlit as st


def apply_custom_css():
    st.markdown("""
    <style>
    /*  Base layout override
       Target the specific Streamlit container to avoid
       fighting the default 6rem top padding */
    .stMainBlockContainer {
        padding: 2.5rem 2rem 2rem;
        max-width: 1100px;
    }

    /* Sidebar ── */
    .stSidebar {
        min-width: 220px;
        max-width: 260px;
    }

    .stSidebar .fs-title {
        font-size: 1.2rem;
    }

    /* ── Hamburger replacement ── */
    [data-testid="collapsedControl"] {
        display: flex;
        align-items: center;
        justify-content: center;
        width: 2.2rem;
        height: 2.2rem;
        background: #1a1a2e;
        border-radius: 6px;
        position: fixed;
        top: 0.6rem;
        left: 0.6rem;
        z-index: 999;
        cursor: pointer;
    }

    [data-testid="collapsedControl"]::before {
        content: "";
        display: block;
        width: 16px;
        height: 2px;
        background: #fff;
        box-shadow: 0 5px 0 #fff, 0 10px 0 #fff;
    }

    button[data-testid="baseButton-headerNoPadding"] {
        display: none;
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
        margin: 0.2rem 0 0.8rem;
    }

    /* ── Section header ── */
    .fs-section {
        display: inline-block;
        font-size: 1.05rem;
        font-weight: 600;
        color: #1a1a2e;
        margin: 0.8rem 0 0.4rem;
        padding-bottom: 0.25rem;
        border-bottom: 2px solid #4a90d9;
    }

    /* ── Card ── */
    .fs-card {
        background: #fff;
        border: 1px solid #e2e2e2;
        border-radius: 10px;
        padding: 1rem 1.2rem;
        margin: 0.3rem 0;
        text-align: center;
        box-shadow: 0 1px 4px rgba(0,0,0,.05);
    }

    .fs-card__label {
        font-size: 0.72rem;
        font-weight: 600;
        color: #555;
        text-transform: uppercase;
        letter-spacing: 0.06em;
        margin-bottom: 0.3rem;
    }

    .fs-card__value {
        font-size: 1.7rem;
        font-weight: 700;
        color: #1a1a2e;
        line-height: 1.2;
    }

    .fs-card__sub {
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

    /* ── Result box — single style, no colour variant ── */
    .fs-result {
        background: #f6fff6;
        border: 1px solid #a9dfbf;
        border-radius: 10px;
        padding: 0.8rem 1rem;
        font-size: 0.88rem;
        color: #333;
        margin: 0.5rem 0;
        line-height: 1.5;
    }

    /* ── Risk badges ── */
    .fs-badge {
        display: inline-block;
        border-radius: 20px;
        padding: 0.25rem 0.8rem;
        font-size: 0.85rem;
        font-weight: 600;
    }

    .fs-badge--high {
        background: #ffe5e5;
        color: #c0392b;
        border: 1px solid #f5b7b1;
    }

    .fs-badge--medium {
        background: #fff3e0;
        color: #d35400;
        border: 1px solid #fad7a0;
    }

    .fs-badge--low {
        background: #e8f8f5;
        color: #1e8449;
        border: 1px solid #a9dfbf;
    }

    /* ── Mobile ── */
    @media screen and (max-width: 768px) {
        .stMainBlockContainer {
            padding: 3rem 1rem 2rem;
        }

        .fs-title {
            font-size: 1.3rem;
        }

        .fs-card__value {
            font-size: 1.4rem;
        }

        .fs-card {
            margin-bottom: 0.5rem;
        }

        .fs-result {
            font-size: 0.8rem;
        }

        .fs-info {
            font-size: 0.8rem;
        }
    }
    </style>
    """, unsafe_allow_html=True)


def metric_card(label, value, sub=None):
    """Reusable metric card — BEM class naming"""
    sub_html = f'<div class="fs-card__sub">{sub}</div>' if sub else ''
    st.markdown(f"""
    <div class="fs-card">
        <div class="fs-card__label">{label}</div>
        <div class="fs-card__value">{value}</div>
        {sub_html}
    </div>
    """, unsafe_allow_html=True)


def risk_badge(risk):
    """Color coded risk badge using BEM modifier classes"""
    modifier = risk.lower()
    st.markdown(
        f'<span class="fs-badge fs-badge--{modifier}">{risk} Risk</span>',
        unsafe_allow_html=True
    )


def section_header(text):
    """Section header with blue underline"""
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


def result_box(text):
    """Green tinted result box — plain text only, no duplicate colour box"""
    st.markdown(
        f'<div class="fs-result">{text}</div>',
        unsafe_allow_html=True
    )

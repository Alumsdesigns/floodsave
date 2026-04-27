# src/styles.py
# Shared CSS and reusable UI components for all dashboard pages
# Call apply_custom_css() once in app.py — all pages inherit styles
# Uses BEM naming convention for CSS classes: block__element--modifier
# Criteria: D7 (professional UX), D8 (clean code)

import streamlit as st


def apply_custom_css():
    """Inject shared CSS into the Streamlit app. Call once in app.py."""
    st.markdown("""
    <style>
    /* Base layout — overrides Streamlit default 6rem top padding */
    .stMainBlockContainer {
        padding: 2.5rem 2rem 2rem;
        max-width: 1100px;
    }

    /* Sidebar width constraints */
    .stSidebar {
        min-width: 220px;
        max-width: 260px;
    }
                
    /* Collapsed sidebar takes zero space on tablet and mobile */
    [data-testid="stSidebar"][aria-expanded="false"] {
        width: 0;
        min-width: 0;
        overflow: hidden;
    }

    .stSidebar .fs-title {
        font-size: 1.2rem;
    }

    /* Hamburger icon — replaces default Streamlit sidebar arrow */
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

    /* Three horizontal lines drawn with box-shadow */
    [data-testid="collapsedControl"]::before {
        content: "";
        display: block;
        width: 16px;
        height: 2px;
        background: #fff;
        box-shadow: 0 5px 0 #fff, 0 10px 0 #fff;
    }

    /* Hide default arrow button */
    button[data-testid="baseButton-headerNoPadding"] {
        display: none;
    }

    /* Page title */
    .fs-title {
        font-size: 1.8rem;
        font-weight: 700;
        color: #1a1a2e;
        margin: 0;
        line-height: 1.2;
    }

    /* Page subtitle */
    .fs-subtitle {
        font-size: 0.95rem;
        color: #555;
        margin: 0.2rem 0 0.8rem;
    }

    /* Section header with blue underline — inline-block keeps width to text length */
    .fs-section {
        display: inline-block;
        font-size: 1.05rem;
        font-weight: 600;
        color: #1a1a2e;
        margin: 0.8rem 0 0.4rem;
        padding-bottom: 0.25rem;
        border-bottom: 2px solid #4a90d9;
    }

    /* Metric card — white box with subtle shadow */
    .fs-card {
        background: #fff;
        border: 1px solid #e2e2e2;
        border-radius: 10px;
        padding: 1rem 1.2rem;
        margin: 0.3rem 0;
        text-align: center;
        box-shadow: 0 1px 4px rgba(0,0,0,.05);
    }

    /* Card label — small uppercase text above value */
    .fs-card__label {
        font-size: 0.72rem;
        font-weight: 600;
        color: #555;
        text-transform: uppercase;
        letter-spacing: 0.06em;
        margin-bottom: 0.3rem;
    }

    /* Card value — large bold number or text */
    .fs-card__value {
        font-size: 1.7rem;
        font-weight: 700;
        color: #1a1a2e;
        line-height: 1.2;
    }

    /* Card subtitle — small descriptive text below value */
    .fs-card__sub {
        font-size: 0.8rem;
        color: #444;
        margin-top: 0.25rem;
    }

    /* Info box — blue left border for contextual information */
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

    /* Result box — green tint for prediction outcomes */
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

    /* Risk badge base styles */
    .fs-badge {
        display: inline-block;
        border-radius: 20px;
        padding: 0.25rem 0.8rem;
        font-size: 0.85rem;
        font-weight: 600;
    }

    /* High risk — red tones */
    .fs-badge--high {
        background: #ffe5e5;
        color: #c0392b;
        border: 1px solid #f5b7b1;
    }

    /* Medium risk — amber tones */
    .fs-badge--medium {
        background: #fff3e0;
        color: #d35400;
        border: 1px solid #fad7a0;
    }

    /* Low risk — green tones */
    .fs-badge--low {
        background: #e8f8f5;
        color: #1e8449;
        border: 1px solid #a9dfbf;
    }

    .fs-back-top {
        position: fixed;
        bottom: 1.5rem;
        right: 1.5rem;
        background: #4a90d9;
        color: #ffffff !important;    /* force white arrow — overrides browser anchor default */
        border: 2px solid #4a90d9;
        border-radius: 8px;
        width: 2.8rem;
        height: 2.8rem;
        font-size: 1.4rem;
        font-weight: 700;
        cursor: pointer;
        z-index: 998;
        display: flex;
        align-items: center;
        justify-content: center;
        box-shadow: 0 2px 8px rgba(0,0,0,0.2);
        text-decoration: none;
        transition: background 0.2s ease, color 0.2s ease;
    }

    .fs-back-top:hover {
        background: #ffffff;
        color: #4a90d9 !important;    /* force blue arrow on hover */
        border: 2px solid #4a90d9;
    }
                
    /* Tablet and mobile — max-width 1024px */
    @media screen and (max-width: 1024px) {

        /* Remove sidebar space when collapsed */
        section[data-testid="stSidebar"] {
            width: 0 !important;
            min-width: 0 !important;
            padding: 0 !important;
        }

        section[data-testid="stSidebar"][aria-expanded="true"] {
            width: 220px !important;
            min-width: 220px !important;
        }

        /* Centre content and prevent overflow */
        .stMainBlockContainer {
            padding: 3rem 1rem 2rem !important;
            margin: 0 auto !important;
            width: 100% !important;
            max-width: 100% !important;
            overflow-x: hidden !important;
        }

        /* Stack columns vertically */
        [data-testid="stHorizontalBlock"] {
            flex-wrap: wrap !important;
        }

        [data-testid="stHorizontalBlock"] > [data-testid="stVerticalBlock"] {
            min-width: 100% !important;
            width: 100% !important;
        }

        /* Typography */
        .fs-title {
            font-size: 1.2rem;
            word-break: break-word;
        }

        .fs-subtitle {
            font-size: 0.85rem;
        }

        .fs-card__value {
            font-size: 1rem;
            word-break: break-word;
        }

        .fs-card {
            margin-bottom: 0.5rem;
        }

        .fs-result {
            font-size: 0.82rem;
        }

        .fs-info {
            font-size: 0.82rem;
            line-height: 1.4;
        }

        .fs-section {
            font-size: 0.95rem;
        }

        /* Hide divider line under map section on mobile */
        .element-container hr {
            display: none;
        }

    </style>
    """, unsafe_allow_html=True)


def metric_card(label, value, sub=None):
    """
    Reusable metric card component.
    Renders a white card with label, large value and optional subtitle.
    Uses BEM class naming: fs-card, fs-card__label, fs-card__value, fs-card__sub
    """
    sub_html = f'<div class="fs-card__sub">{sub}</div>' if sub else ''
    st.markdown(f"""
    <div class="fs-card">
        <div class="fs-card__label">{label}</div>
        <div class="fs-card__value">{value}</div>
        {sub_html}
    </div>
    """, unsafe_allow_html=True)


def risk_badge(risk):
    """
    Colour coded risk badge.
    Accepts High, Medium or Low — applies matching BEM modifier class.
    """
    modifier = risk.lower()
    st.markdown(
        f'<span class="fs-badge fs-badge--{modifier}">{risk} Risk</span>',
        unsafe_allow_html=True
    )


def section_header(text):
    """Section header with blue underline — width matches text length."""
    st.markdown(
        f'<div class="fs-section">{text}</div>',
        unsafe_allow_html=True
    )


def info_box(text):
    """Info box with left blue border for contextual information."""
    st.markdown(
        f'<div class="fs-info">{text}</div>',
        unsafe_allow_html=True
    )


def result_box(text):
    """Green tinted result box for prediction outcomes."""
    st.markdown(
        f'<div class="fs-result">{text}</div>',
        unsafe_allow_html=True
    )

def back_to_top():
    """
    Back to top anchor link — uses named anchor, no JavaScript needed.
    Avoids Streamlit React onclick conflict.
    """
    st.markdown(
        '<a class="fs-back-top" href="#floodsave-top">↑</a>',
        unsafe_allow_html=True
    )
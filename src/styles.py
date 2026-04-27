# src/styles.py
# Shared CSS and reusable UI components for all dashboard pages
# Call apply_custom_css() once in app.py — all pages inherit styles
# Uses BEM naming convention for CSS classes: block__element--modifier
# Typography: Plus Jakarta Sans (headings) + DM Sans (body) — professional data app pairing
# Criteria: D7 (professional UX), D8 (clean code)

import streamlit as st


def apply_custom_css():
    """Inject shared CSS into the Streamlit app. Call once in app.py."""
    st.markdown("""
    <style>
    /* ============================================================
       FONTS
       Plus Jakarta Sans — geometric, modern for headings (H1/H2)
       DM Sans — neutral, highly legible for body and UI text
       Both from Google Fonts — open source, no licence required
    ============================================================ */
    @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@600;700;800&family=DM+Sans:wght@400;500;600&display=swap');

    /* ============================================================
       TYPOGRAPHIC SCALE — 6 levels, consistent ratio ~1.25
       Level 1 (H1)  — page title        2.2rem / 800 / Plus Jakarta Sans
       Level 2 (H2)  — section header    1.15rem / 600 / Plus Jakarta Sans
       Level 3       — card value        1.75rem / 700 / Plus Jakarta Sans
       Level 4       — card label        0.70rem / 600 / DM Sans uppercase
       Level 5       — body / info       0.90rem / 400 / DM Sans
       Level 6       — small / sub       0.78rem / 400 / DM Sans
    ============================================================ */

    /* Base — DM Sans for all elements, overridden per level below */
    * {
        font-family: 'DM Sans', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
    }

    /* ============================================================
       BASE LAYOUT
    ============================================================ */

    /* Overrides Streamlit default 6rem top padding */
    .stMainBlockContainer {
        padding: 2.5rem 2rem 2rem;
        max-width: 1100px;
    }

    /* ============================================================
       SIDEBAR
    ============================================================ */

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
        font-size: 1.1rem;
    }

    /* ============================================================
       HAMBURGER ICON — replaces default Streamlit sidebar arrow
    ============================================================ */

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

    /* ============================================================
       TYPOGRAPHY — LEVEL 1 (H1) — Page title
       Font: Plus Jakarta Sans 800
       Size: 2.2rem desktop / 1.3rem mobile
       Usage: one per page, identifies the page
    ============================================================ */
    .fs-title {
        font-family: 'Plus Jakarta Sans', sans-serif;
        font-size: 2.2rem;
        font-weight: 800;
        color: #1a1a2e;
        margin: 0;
        line-height: 1.15;
        letter-spacing: -0.03em;
    }

    /* ============================================================
       TYPOGRAPHY — LEVEL 2 (H2) — Page subtitle
       Font: DM Sans 400
       Size: 0.95rem
       Usage: one per page, below the H1 title
    ============================================================ */
    .fs-subtitle {
        font-family: 'DM Sans', sans-serif;
        font-size: 0.95rem;
        font-weight: 400;
        color: #555;
        margin: 0.25rem 0 0.9rem;
        line-height: 1.5;
        letter-spacing: 0;
    }

    /* ============================================================
       TYPOGRAPHY — LEVEL 2 (H2) — Section header
       Font: Plus Jakarta Sans 600
       Size: 1.15rem
       Usage: divides page into named sections
    ============================================================ */
    .fs-section {
        display: inline-block;
        font-family: 'Plus Jakarta Sans', sans-serif;
        font-size: 1.15rem;
        font-weight: 600;
        color: #1a1a2e;
        margin: 0.9rem 0 0.45rem;
        padding-bottom: 0.28rem;
        border-bottom: 2px solid #4a90d9;
        line-height: 1.3;
        letter-spacing: -0.01em;
    }

    /* ============================================================
       METRIC CARD — white box with shadow
    ============================================================ */
    .fs-card {
        background: #fff;
        border: 1px solid #e2e2e2;
        border-radius: 10px;
        padding: 1rem 1.2rem;
        margin: 0.3rem 0;
        text-align: center;
        box-shadow: 0 1px 4px rgba(0, 0, 0, 0.05);
    }

    /* ============================================================
       TYPOGRAPHY — LEVEL 4 — Card label
       Font: DM Sans 600 uppercase
       Size: 0.70rem
       Usage: small descriptor above the card value
    ============================================================ */
    .fs-card__label {
        font-family: 'DM Sans', sans-serif;
        font-size: 0.70rem;
        font-weight: 600;
        color: #555;
        text-transform: uppercase;
        letter-spacing: 0.08em;
        margin-bottom: 0.3rem;
        line-height: 1.4;
    }

    /* ============================================================
       TYPOGRAPHY — LEVEL 3 — Card value (display number)
       Font: Plus Jakarta Sans 700
       Size: 1.75rem
       Usage: the primary metric — station count, accuracy score etc
    ============================================================ */
    .fs-card__value {
        font-family: 'Plus Jakarta Sans', sans-serif;
        font-size: 1.75rem;
        font-weight: 700;
        color: #1a1a2e;
        line-height: 1.15;
        letter-spacing: -0.02em;
    }

    /* ============================================================
       TYPOGRAPHY — LEVEL 6 — Card subtitle
       Font: DM Sans 400
       Size: 0.78rem
       Usage: supporting description below card value
    ============================================================ */
    .fs-card__sub {
        font-family: 'DM Sans', sans-serif;
        font-size: 0.78rem;
        font-weight: 400;
        color: #444;
        margin-top: 0.28rem;
        line-height: 1.45;
    }

    /* ============================================================
       INFO BOX — blue left border for contextual information
       TYPOGRAPHY — LEVEL 5 — body text
       Font: DM Sans 400
       Size: 0.90rem
    ============================================================ */
    .fs-info {
        background: #f0f7ff;
        border-left: 3px solid #4a90d9;
        border-radius: 0 6px 6px 0;
        padding: 0.75rem 1rem;
        font-family: 'DM Sans', sans-serif;
        font-size: 0.90rem;
        font-weight: 400;
        color: #333;
        margin: 0.5rem 0;
        line-height: 1.6;
    }

    /* ============================================================
       RESULT BOX — green tint for prediction outcomes
       TYPOGRAPHY — LEVEL 5 — body text
       Font: DM Sans 400
       Size: 0.90rem
    ============================================================ */
    .fs-result {
        background: #f6fff6;
        border: 1px solid #a9dfbf;
        border-radius: 10px;
        padding: 0.85rem 1rem;
        font-family: 'DM Sans', sans-serif;
        font-size: 0.90rem;
        font-weight: 400;
        color: #333;
        margin: 0.5rem 0;
        line-height: 1.6;
    }

    /* ============================================================
       RISK BADGES — semantic colour per risk level
    ============================================================ */

    /* Badge base */
    .fs-badge {
        display: inline-block;
        border-radius: 20px;
        padding: 0.25rem 0.85rem;
        font-family: 'DM Sans', sans-serif;
        font-size: 0.85rem;
        font-weight: 600;
        line-height: 1.4;
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

    /* ============================================================
       BACK TO TOP BUTTON
       Fixed bottom right — blue default, inverts on hover
    ============================================================ */
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
        box-shadow: 0 2px 8px rgba(0, 0, 0, 0.2);
        text-decoration: none;
        transition: background 0.2s ease, color 0.2s ease;
    }

    /* Invert colours on hover — blue arrow on white background */
    .fs-back-top:hover {
        background: #ffffff;
        color: #4a90d9 !important;
        border: 2px solid #4a90d9;
    }

    /* ============================================================
       RESPONSIVE — tablet and mobile max-width 1024px
       Collapses columns, reduces font sizes, adjusts spacing
    ============================================================ */
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

        /* Centre content and prevent horizontal overflow */
        .stMainBlockContainer {
            padding: 3rem 1rem 2rem !important;
            margin: 0 auto !important;
            width: 100% !important;
            max-width: 100% !important;
            overflow-x: hidden !important;
        }

        /* Stack columns vertically on small screens */
        [data-testid="stHorizontalBlock"] {
            flex-wrap: wrap !important;
        }

        [data-testid="stHorizontalBlock"] > [data-testid="stVerticalBlock"] {
            min-width: 100% !important;
            width: 100% !important;
        }

        /* H1 scales down on mobile */
        .fs-title {
            font-size: 1.3rem;
            letter-spacing: -0.01em;
            word-break: break-word;
        }

        /* H2 subtitle scales down */
        .fs-subtitle {
            font-size: 0.85rem;
        }

        /* Section header scales down */
        .fs-section {
            font-size: 1rem;
        }

        /* Card value scales down — prevents overflow on narrow screens */
        .fs-card__value {
            font-size: 1.1rem;
            word-break: break-word;
        }

        .fs-card {
            margin-bottom: 0.5rem;
        }

        /* Body text tightens line height on small screens */
        .fs-result,
        .fs-info {
            font-size: 0.82rem;
            line-height: 1.45;
        }

        /* Hide divider line under map section on mobile */
        .element-container hr {
            display: none;
        }
    }

    </style>
    """, unsafe_allow_html=True)


def metric_card(label, value, sub=None):
    """
    Reusable metric card component.
    Renders a white card with label (H4/DM Sans), large value (H3/Plus Jakarta Sans)
    and optional subtitle (small/DM Sans).
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
    Red for High, amber for Medium, green for Low.
    """
    modifier = risk.lower()
    st.markdown(
        f'<span class="fs-badge fs-badge--{modifier}">{risk} Risk</span>',
        unsafe_allow_html=True
    )


def section_header(text):
    """
    Section header — H2 level with blue underline.
    Plus Jakarta Sans 600 — width matches text length via inline-block.
    """
    st.markdown(
        f'<div class="fs-section">{text}</div>',
        unsafe_allow_html=True
    )


def info_box(text):
    """
    Info box with left blue border for contextual information.
    DM Sans body text — light blue background, used for explanations and instructions.
    """
    st.markdown(
        f'<div class="fs-info">{text}</div>',
        unsafe_allow_html=True
    )


def result_box(text):
    """
    Green tinted result box for prediction outcomes.
    DM Sans body text — used to display flood risk prediction results.
    """
    st.markdown(
        f'<div class="fs-result">{text}</div>',
        unsafe_allow_html=True
    )


def back_to_top():
    """
    Back to top anchor link — fixed position bottom right on all pages.
    Uses named anchor href — no JavaScript needed.
    Blue default state, inverts to white background on hover.
    Avoids Streamlit React onclick conflict by using plain HTML anchor.
    """
    st.markdown(
        '<a class="fs-back-top" href="#floodsave-top">↑</a>',
        unsafe_allow_html=True
    )
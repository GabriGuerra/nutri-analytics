import streamlit as st

def load_layout():
    st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');

    /* ===================== BASE ===================== */
    html, body, [class*="css"] {
        font-family: 'Inter', sans-serif;
        background-color: #F8FAFC;
        color: #1F2933;
    }

    /* ===================== SIDEBAR ===================== */
    [data-testid="stSidebar"] {
        background: #FFFFFF;
        border-right: 1px solid #E5E7EB;
    }

    .profile-box {
        padding: 1.6rem 0;
        border-bottom: 1px dashed #E5E7EB;
        margin-bottom: 1.8rem;
    }

    .profile-name {
        color: #111827;
        font-weight: 700;
        font-size: 1.05rem;
        letter-spacing: -0.02em;
    }

    .profile-role {
        color: #6B7280;
        font-weight: 600;
        font-size: 0.72rem;
        text-transform: uppercase;
        letter-spacing: 0.1em;
    }

    .profile-desc {
        color: #6B7280;
        font-size: 0.8rem;
        margin-top: 6px;
    }

    /* ===================== SECTIONS ===================== */
    .section-title {
        font-size: 0.72rem;
        font-weight: 700;
        color: #374151;
        text-transform: uppercase;
        letter-spacing: 0.14em;
        margin-bottom: 18px;
        border-left: 3px solid #D1D5DB;
        padding-left: 10px;
    }

    /* ===================== INPUTS ===================== */
    .stMultiSelect div[data-baseweb="select"],
    .stSelectbox div[data-baseweb="select"] {
        background-color: #FFFFFF;
        border-radius: 10px;
        border: 1px solid #D1D5DB;
        transition: all 0.2s ease-in-out;
    }

    .stMultiSelect div[data-baseweb="select"]:hover,
    .stSelectbox div[data-baseweb="select"]:hover {
        border-color: #9CA3AF;
    }

    .stMultiSelect span[data-baseweb="tag"] {
        background-color: #F3F4F6 !important;
        color: #111827 !important;
        border-radius: 999px;
        font-weight: 500;
    }

    div[aria-selected="true"] {
        background-color: #E5E7EB !important;
        color: #111827 !important;
    }

    /* ===================== DATAFRAME ===================== */
    [data-testid="stDataFrame"] {
        border: 1px solid #E5E7EB;
        border-radius: 14px;
        background-color: #FFFFFF;
    }

    [data-testid="stDataFrame"] thead tr th {
        background-color: #F3F4F6;
        color: #111827;
        font-weight: 600;
    }

    [data-testid="stDataFrame"] tbody tr:hover {
        background-color: #F9FAFB;
    }

    /* ===================== TEXTOS ===================== */
    h1, h2, h3 {
        color: #111827 !important;
        font-weight: 700;
    }

    p {
        color: #4B5563 !important;
    }

    /* ===================== SCROLLBAR ===================== */
    ::-webkit-scrollbar {
        width: 8px;
    }

    ::-webkit-scrollbar-thumb {
        background-color: #D1D5DB;
        border-radius: 20px;
    }
    </style>
    """, unsafe_allow_html=True)

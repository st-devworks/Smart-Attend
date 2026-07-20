import streamlit as st


def load_css():

    st.markdown("""
    <style>

    /* ==========================================
       FONT
    ========================================== */

    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700;800&display=swap');

    html, body, [class*="css"]{
        font-family:'Poppins',sans-serif;
    }


    /* ==========================================
       REMOVE STREAMLIT DEFAULT HEADER
    ========================================== */

    header{
        visibility:hidden;
    }

    footer{
        visibility:hidden;
    }

    #MainMenu{
        visibility:hidden;
    }

    div[data-testid="stToolbar"]{
        display:none;
    }

    header[data-testid="stHeader"]{
        display:none;
    }

    div[data-testid="stDecoration"]{
        display:none;
    }


    /* ==========================================
       MAIN BACKGROUND
    ========================================== */

    .stApp{
        background:#0F172A;
        color:white;
    }

    div[data-testid="stAppViewContainer"] > .main{
        padding-top:0rem;
    }

    .block-container{

        padding-top:1rem !important;

        padding-left:2rem;

        padding-right:2rem;

        padding-bottom:2rem;

        max-width:1400px;

    }


    /* ==========================================
       SIDEBAR
    ========================================== */

    section[data-testid="stSidebar"]{

        background:#111827;

        border-right:1px solid #243244;

    }

    section[data-testid="stSidebar"] *{

        color:white;

    }

    section[data-testid="stSidebarNav"]{

        padding-top:20px;

    }


    /* ==========================================
       TITLES
    ========================================== */

    h1{

        color:white;

        font-size:48px;

        font-weight:800;

        margin-bottom:5px;

    }

    h2{

        color:white;

        font-weight:700;

    }

    h3{

        color:white;

        font-weight:600;

    }

    p{

        color:#CBD5E1;

    }


    /* ==========================================
       METRIC CARDS
    ========================================== */

    div[data-testid="stMetric"]{

        background:#1E293B;

        border:1px solid #334155;

        border-radius:18px;

        padding:22px;

        box-shadow:0px 8px 25px rgba(0,0,0,.35);

        transition:0.25s;

    }

    div[data-testid="stMetric"]:hover{

        transform:translateY(-5px);

        border:1px solid #3B82F6;

    }

    div[data-testid="stMetricLabel"]{

        color:#94A3B8;

        font-size:15px;

        font-weight:600;

    }

    div[data-testid="stMetricValue"]{

        color:white;

        font-size:34px;

        font-weight:800;

    }


    /* ==========================================
       BUTTONS
    ========================================== */

    .stButton>button{

        width:100%;

        background:#2563EB;

        color:white;

        border:none;

        border-radius:12px;

        padding:12px;

        font-size:16px;

        font-weight:600;

        transition:0.25s;

    }

    .stButton>button:hover{

        background:#1D4ED8;

        transform:scale(1.02);

    }


    /* ==========================================
       TEXT INPUT
    ========================================== */

    .stTextInput input{

        background:#1E293B !important;

        color:white !important;

        border:1px solid #334155 !important;

        border-radius:10px !important;

    }

    .stTextInput input:focus{

        border:1px solid #3B82F6 !important;

        box-shadow:none !important;

    }


    /* ==========================================
       SELECT BOX
    ========================================== */

    .stSelectbox div[data-baseweb="select"]{

        background:#1E293B;

        border-radius:10px;

        border:1px solid #334155;

    }


    /* ==========================================
       DATAFRAME
    ========================================== */

    div[data-testid="stDataFrame"]{

        border-radius:15px;

        overflow:hidden;

        border:1px solid #334155;

    }


    /* ==========================================
       ALERTS
    ========================================== */

    div[data-testid="stAlert"]{

        border-radius:12px;

    }


    /* ==========================================
       DIVIDER
    ========================================== */

    hr{

        border:1px solid #334155;

    }


    /* ==========================================
       SCROLLBAR
    ========================================== */

    ::-webkit-scrollbar{

        width:10px;

        height:10px;

    }

    ::-webkit-scrollbar-track{

        background:#111827;

    }

    ::-webkit-scrollbar-thumb{

        background:#475569;

        border-radius:20px;

    }

    ::-webkit-scrollbar-thumb:hover{

        background:#64748B;

    }
    

    </style>
    """, unsafe_allow_html=True)
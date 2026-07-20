import streamlit as st

st.set_page_config(
    page_title="SmartAttend",
    page_icon="🎓",
    layout="wide"
)

from login import login

if "logged_in" not in st.session_state or not st.session_state.logged_in:
    st.markdown("""
    <style>
    section[data-testid="stSidebar"]{
        display:none;
    }
    </style>
    """, unsafe_allow_html=True)
# -----------------------------
# LOGIN
# -----------------------------

if not login():
    st.stop()

# -----------------------------
# PAGES
# -----------------------------

dashboard = st.Page(
    "pages/1_Dashboard.py",
    title="Dashboard",
    icon="📊"
)

students = st.Page(
    "pages/2_Students.py",
    title="Students",
    icon="👨‍🎓"
)

register = st.Page(
    "pages/3_Register_Face.py",
    title="Register Face",
    icon="📷"
)

train = st.Page(
    "pages/4_Train_Model.py",
    title="Train Model",
    icon="🧠"
)

attendance = st.Page(
    "pages/5_Take_Attendance.py",
    title="Take Attendance",
    icon="✅"
)

history = st.Page(
    "pages/6_Attendance_History.py",
    title="Attendance History",
    icon="📜"
)

email = st.Page(
    "pages/7_Email_Reports.py",
    title="Email Reports",
    icon="📧"
)

# -----------------------------
# SIDEBAR
# -----------------------------

with st.sidebar:

    st.title("🎓 SmartAttend")

    st.success("Administrator")

    st.divider()

    if st.button("🚪 Logout", use_container_width=True):

        st.session_state.logged_in = False
        st.rerun()

# -----------------------------
# NAVIGATION
# -----------------------------

pg = st.navigation(
    [
        dashboard,
        students,
        register,
        train,
        attendance,
        history,
        email
    ]
)

pg.run()
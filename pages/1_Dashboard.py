import streamlit as st
import pandas as pd
import os
from style import load_css

from database import get_students, get_attendance
load_css()
# -----------------------------
# Load Data
# -----------------------------
students = get_students()
attendance = get_attendance()

students = [dict(row) for row in students]
attendance = [dict(row) for row in attendance]

total_students = len(students)
total_records = len(attendance)

today = pd.Timestamp.today().strftime("%Y-%m-%d")

today_attendance = len(
    [record for record in attendance if record["date"] == today]
)

model_status = (
    "✅ Trained"
    if os.path.exists("trainer/trainer.yml")
    else "❌ Not Trained"
)

# -----------------------------
# Dashboard Header
# -----------------------------
st.title("🎓 SmartAttend Dashboard")

st.caption("AI Powered Face Recognition Attendance Management System")

st.divider()

# -----------------------------
# Dashboard Metrics
# -----------------------------
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("👨 Total Students", total_students)

with col2:
    st.metric("📋 Attendance Records", total_records)

with col3:
    st.metric("📅 Today's Attendance", today_attendance)



st.divider()

# -----------------------------
# Recent Attendance
# -----------------------------
st.subheader("🕒 Recent Attendance")

if attendance:

    df = pd.DataFrame(attendance)

    st.dataframe(
        df.head(10),
        use_container_width=True,
        hide_index=True
    )

else:
    st.info("No attendance records available.")

st.divider()

st.caption("© 2026 SmartAttend | Developed by Shikhar Tiwari")
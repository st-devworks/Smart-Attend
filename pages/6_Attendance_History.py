import streamlit as st
import pandas as pd
from io import BytesIO
from style import load_css
from database import (
    get_attendance,
    get_attendance_by_date
)
load_css()
st.title("📋 Attendance History")

selected_date = st.date_input(
    "Filter by Date"
)

records = get_attendance_by_date(
    str(selected_date)
)

if records:

    df = pd.DataFrame(records)
    buffer = BytesIO()

    with pd.ExcelWriter(buffer, engine="openpyxl") as writer:
        df.to_excel(writer, index=False, sheet_name="Attendance")

    buffer.seek(0)

    st.dataframe(
        df,
        use_container_width=True
    )
    st.download_button(
    label="📥 Download Attendance Excel",
    data=buffer,
    file_name="attendance_report.xlsx",
    mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
)

else:

    st.info("No Attendance Records Found.")
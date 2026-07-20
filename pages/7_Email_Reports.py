import streamlit as st

from database import (
    get_students,
    get_monthly_attendance
)

from EmailsUtils import send_monthly_report


st.title("📧 Email Reports")

students = get_students()

if not students:
    st.warning("No students found.")
    st.stop()


month = st.number_input(
    "Month",
    min_value=1,
    max_value=12,
    value=7
)

year = st.number_input(
    "Year",
    min_value=2025,
    max_value=2035,
    value=2026
)

if st.button("📧 Send Reports to All Students"):

    success = 0
    failed = 0

    progress = st.progress(0)

    status = st.empty()

    total = len(students)

    for index, student in enumerate(students):

        report = get_monthly_attendance(
            student["id"],
            month,
            year
        )

        result = send_monthly_report(
            student["email"],
            student["name"],
            report,
            month,
            year
        )

        if result is True:
            success += 1
            status.success(f"✅ Sent to {student['name']}")
        else:
            failed += 1
            status.error(f"❌ Failed : {student['name']}")

        progress.progress((index + 1) / total)

    st.divider()

    st.success(f"🎉 {success} reports sent successfully.")

    if failed > 0:
        st.warning(f"{failed} emails failed to send.")
import streamlit as st
from style import load_css
from database import (
    add_student,
    get_students,
    delete_student,
    update_student
)
load_css()
st.title("👨 Student Management")

if "edit_student" not in st.session_state:
    st.session_state.edit_student = None

if "delete_student" not in st.session_state:
    st.session_state.delete_student = None

# -----------------------
# Add Student
# -----------------------

st.subheader("➕ Add Student")

with st.form("student_form"):
    name = st.text_input("Student Name")
    roll = st.text_input("Roll Number")
    email = st.text_input("Email")
    course = st.text_input("Course")

    submit = st.form_submit_button("Add Student")

    if submit:

        if name and roll:

            try:
                add_student(name, roll, email, course)
                st.success("Student Added Successfully!")
                st.rerun()

            except Exception as e:
                st.error(f"Error : {e}")

        else:
            st.warning("Name and Roll Number are required.")

# -----------------------
# Student List
# -----------------------

st.divider()

# -----------------------
# Edit Student
# -----------------------

if st.session_state.edit_student:

    st.subheader("✏️ Edit Student")

    student = st.session_state.edit_student

    with st.form("edit_form"):

        edit_name = st.text_input(
            "Student Name",
            value=student["name"]
        )

        edit_roll = st.text_input(
            "Roll Number",
            value=student["roll"]
        )

        edit_email = st.text_input(
            "Email",
            value=student["email"]
        )

        edit_course = st.text_input(
            "Course",
            value=student["course"]
        )

        update = st.form_submit_button("Update Student")
        if update:
            try:
                update_student(
                    student["id"],
                    edit_name,
                    edit_roll,
                    edit_email,
                    edit_course
                )

                st.success("Student Updated Successfully!")

                st.session_state.edit_student = None

                st.rerun()

            except Exception as e:
                st.error(f"Error: {e}")

# -----------------------
# Delete Confirmation
# -----------------------

if st.session_state.delete_student:

    student = st.session_state.delete_student

    st.warning(
        f"Are you sure you want to delete {student['name']}?"
    )

    col1, col2 = st.columns(2)

    with col1:
        if st.button("✅ Yes, Delete"):

            delete_student(student["id"])

            st.success("Student Deleted Successfully!")

            st.session_state.delete_student = None

            st.rerun()

    with col2:
        if st.button("❌ Cancel"):

            st.session_state.delete_student = None

            st.rerun()

st.subheader("📋 Student List")
search = st.text_input("🔍 Search by Name or Roll Number")



students = get_students()

if search:
    students = [
        student for student in students
        if search.lower() in student["name"].lower()
        or search.lower() in student["roll"].lower()
    ]

if students:

    for student in students:

        col1, col2, col3 = st.columns([8,1,1])
        with col1:
            st.write(
                f"**{student['roll']}** | {student['name']} | {student['email']} | {student['course']}"
            )

        with col2:
            if st.button("✏️", key=f"edit_{student['id']}", use_container_width=True):
                st.session_state.edit_student = student

        with col3:
            if st.button("🗑️", key=f"delete_{student['id']}", use_container_width=True):
                st.session_state.delete_student = student
else:
    st.info("No Students Added Yet.")
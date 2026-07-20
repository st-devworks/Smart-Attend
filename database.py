import sqlite3
from config import DATABASE_PATH
from datetime import datetime


def get_connection():
    """Create database connection"""
    conn = sqlite3.connect(DATABASE_PATH)
    conn.row_factory = sqlite3.Row
    return conn


def create_tables():
    """Create all required tables"""

    conn = get_connection()
    cursor = conn.cursor()

    # Students Table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS students(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            roll TEXT UNIQUE NOT NULL,
            email TEXT,
            course TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)

    # Attendance Table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS attendance(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            student_id INTEGER,
            date TEXT,
            time TEXT,
            status TEXT,
            FOREIGN KEY(student_id) REFERENCES students(id)
        )
    """)

    conn.commit()
    conn.close()


def add_student(name, roll, email, course):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO students(name, roll, email, course)
        VALUES (?, ?, ?, ?)
    """, (name, roll, email, course))

    conn.commit()
    conn.close()


def get_students():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT * FROM students
        ORDER BY id DESC
    """)

    students = cursor.fetchall()

    conn.close()

    return students


def delete_student(student_id):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        DELETE FROM students
        WHERE id=?
    """, (student_id,))



    conn.commit()
    conn.close()

def get_dashboard_stats():
    conn = get_connection()
    cursor = conn.cursor()

    # Total students
    cursor.execute("SELECT COUNT(*) FROM students")
    total_students = cursor.fetchone()[0]

    # Total attendance records
    cursor.execute("SELECT COUNT(*) FROM attendance")
    total_attendance = cursor.fetchone()[0]

    conn.close()

    return {
        "students": total_students,
        "attendance": total_attendance
    }

def update_student(student_id, name, roll, email, course):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        UPDATE students
        SET name=?, roll=?, email=?, course=?
        WHERE id=?
    """, (name, roll, email, course, student_id))

    conn.commit()
    conn.close()

def get_student_by_id(student_id):
    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute("""
        SELECT * FROM students
        WHERE id=?
    """, (student_id,))

    student = cursor.fetchone()

    conn.close()

    return student



def mark_attendance(student_id):
    conn = get_connection()
    cursor = conn.cursor()

    today = datetime.now().strftime("%Y-%m-%d")
    current_time = datetime.now().strftime("%H:%M:%S")

    # Check if attendance already exists today
    cursor.execute("""
        SELECT * FROM attendance
        WHERE student_id=? AND date=?
    """, (student_id, today))

    existing = cursor.fetchone()

    if not existing:
        cursor.execute("""
            INSERT INTO attendance(student_id, date, time, status)
            VALUES (?, ?, ?, ?)
        """, (student_id, today, current_time, "Present"))

        conn.commit()

    conn.close()

def get_attendance():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT
            attendance.id,
            students.roll,
            students.name,
            attendance.date,
            attendance.time,
            attendance.status
        FROM attendance
        JOIN students
        ON attendance.student_id = students.id
        ORDER BY attendance.date DESC, attendance.time DESC
    """)

    rows = cursor.fetchall()

    conn.close()

    return rows

def get_attendance_by_date(selected_date):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT
            attendance.id,
            students.roll,
            students.name,
            attendance.date,
            attendance.time,
            attendance.status
        FROM attendance
        JOIN students
        ON attendance.student_id = students.id
        WHERE attendance.date = ?
        ORDER BY attendance.time DESC
    """, (selected_date,))

    rows = cursor.fetchall()

    conn.close()

    return rows

def get_monthly_attendance(student_id, month, year):
    """
    Returns attendance summary for one student in a given month.
    """

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT COUNT(*)
        FROM attendance
        WHERE student_id = ?
        AND status = 'Present'
        AND strftime('%m', date) = ?
        AND strftime('%Y', date) = ?
    """, (
        student_id,
        f"{month:02d}",
        str(year)
    ))

    present_days = cursor.fetchone()[0]

    cursor.execute("""
        SELECT COUNT(DISTINCT date)
        FROM attendance
        WHERE strftime('%m', date) = ?
        AND strftime('%Y', date) = ?
    """, (
        f"{month:02d}",
        str(year)
    ))

    total_days = cursor.fetchone()[0]

    conn.close()

    if total_days == 0:
        percentage = 0
    else:
        percentage = round((present_days / total_days) * 100, 2)

    return {
        "present_days": present_days,
        "total_days": total_days,
        "percentage": percentage
    }
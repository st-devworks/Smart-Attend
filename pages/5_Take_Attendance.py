import streamlit as st
import cv2
import os
from datetime import datetime
from style import load_css
from database import (
    get_student_by_id,
    get_connection,
    mark_attendance
)
load_css()
st.title("📸 Take Attendance")

if not os.path.exists("trainer/trainer.yml"):
    st.error("Please train the model first.")
    st.stop()

recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read("trainer/trainer.yml")

face_detector = cv2.CascadeClassifier(
    "assets/haarcascade_frontalface_default.xml"
)

if face_detector.empty():
    st.error("Could not load Haar Cascade.")
    st.stop()

if st.button("Start Attendance"):

    cam = cv2.VideoCapture(0)

    if not cam.isOpened():
        st.error("Could not open webcam.")
        st.stop()
    
    marked_students = set()

    while True:

        ret, img = cam.read()

        if not ret:
            break

        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        faces = face_detector.detectMultiScale(
            gray,
            scaleFactor=1.2,
            minNeighbors=5
        )

        for (x, y, w, h) in faces:

            face = gray[y:y+h, x:x+w]

            student_id, confidence = recognizer.predict(face)

            if confidence < 70:

                student = get_student_by_id(student_id)

                if student:

                    name = student["name"]

                    if student_id not in marked_students:
                        mark_attendance(student_id)
                        marked_students.add(student_id)

                    cv2.putText(
                        img,
                        f"{name} - Present",
                        (x, y - 10),
                        cv2.FONT_HERSHEY_SIMPLEX,
                        0.8,
                        (0, 255, 0),
                        2
                    )

                    cv2.rectangle(
                        img,
                        (x, y),
                        (x+w, y+h),
                        (0, 255, 0),
                        2
                    )

                    continue

            else:

                cv2.putText(
                    img,
                    "Unknown",
                    (x, y - 10),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.8,
                    (0, 0, 255),
                    2
                )

                cv2.rectangle(
                    img,
                    (x, y),
                    (x+w, y+h),
                    (0, 0, 255),
                    2
                )

        cv2.imshow("Attendance", img)

        key = cv2.waitKey(1)

        if key == 27:
            break

        if cv2.getWindowProperty("Attendance", cv2.WND_PROP_VISIBLE) < 1:
            break

    cam.release()
    cv2.destroyAllWindows()
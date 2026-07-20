import streamlit as st
import cv2
import os
from database import get_students
from style import load_css
load_css()
st.title("📷 Register Face")

students = get_students()

if not students:
    st.warning("Please add students first.")
    st.stop()

student_options = {
    f"{student['roll']} - {student['name']}": student
    for student in students
}

selected = st.selectbox(
    "Select Student",
    list(student_options.keys())
)

student = student_options[selected]

if st.button("Start Capture"):

    os.makedirs("dataset", exist_ok=True)

    face_detector = cv2.CascadeClassifier(
        "assets/haarcascade_frontalface_default.xml"
    )
    if face_detector.empty():
        st.error("Could not load Haar Cascade file.")
        st.stop()

    cam = cv2.VideoCapture(0)
    if not cam.isOpened():
        st.error("Could not open webcam.")
        st.stop()

    count = 0

    while True:


        ret, img = cam.read()

        if not ret:
            break

        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        faces = face_detector.detectMultiScale(
            gray,
            scaleFactor=1.3,
            minNeighbors=5
        )

        for (x, y, w, h) in faces:

            count += 1

            face = gray[y:y+h, x:x+w]

            cv2.imwrite(
                f"dataset/User.{student['id']}.{count}.jpg",
                face
            )

            cv2.rectangle(
                img,
                (x, y),
                (x+w, y+h),
                (0, 255, 0),
                2
            )

            cv2.putText(
                img,
                f"Images: {count}/30",
                (20, 30),
                cv2.FONT_HERSHEY_SIMPLEX,
                1,
                (0, 255, 0),
                2
            )

        cv2.imshow("Register Face", img)

        if cv2.waitKey(1) == 27 or count >= 30:
            break

    cam.release()
    cv2.destroyAllWindows()

    st.success("Face Registered Successfully!")
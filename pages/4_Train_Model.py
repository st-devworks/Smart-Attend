import streamlit as st
import cv2
import os
import numpy as np
from PIL import Image
from style import load_css
load_css()
st.title("🧠 Train Face Model")

if st.button("Train Model"):

    recognizer = cv2.face.LBPHFaceRecognizer_create()

    dataset_path = "dataset"

    image_paths = [
        os.path.join(dataset_path, f)
        for f in os.listdir(dataset_path)
    ]

    faces = []
    ids = []

    for image_path in image_paths:

        gray_image = Image.open(image_path).convert("L")

        image_np = np.array(gray_image, "uint8")

        student_id = int(
            os.path.split(image_path)[-1].split(".")[1]
        )

        faces.append(image_np)

        ids.append(student_id)

    recognizer.train(faces, np.array(ids))

    os.makedirs("trainer", exist_ok=True)

    recognizer.save("trainer/trainer.yml")

    st.success("Model Trained Successfully!")
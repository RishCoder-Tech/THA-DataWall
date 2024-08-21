import streamlit as st
import PIL.Image
import numpy as np
import cv2

st.title("Checkmark Counter")

uploaded_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    # Read the image
    image = PIL.Image.open(uploaded_file)
    image = np.array(image)

    # Convert the image to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Threshold the image to create a binary image
    _, thresh = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)

    # Find contours in the image
    contours, hierarchy = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Count the number of checkmarks
    checkmark_count = 0
    for contour in contours:
        # Approximate the contour
        approx = cv2.approxPolyDP(contour, 0.01 * cv2.arcLength(contour, True), True)

        # Check if the contour is a checkmark
        if len(approx) == 4:
            checkmark_count += 1

    # Display the image and the checkmark count
    st.image(image, caption="Uploaded Image", width=400)
    st.write(f"Number of checkmarks: {checkmark_count}")
import streamlit as st
import numpy as np
from PIL import Image
from io import BytesIO
import cv2
import base64

st.set_page_config(layout="wide", page_title="Color to B&W Image")

st.write("## Color to B&W Image")
st.write(
    "Upload an image to convert it into B&W image. Full quality images can be downloaded from the sidebar."
)
st.sidebar.write("## Upload and download :gear:")


# Download the fixed image
def convert_image(img):
    buf = BytesIO()
    img.save(buf, format="PNG")
    byte_im = buf.getvalue()
    return byte_im

def colourtobg(image):
    numpy_array = np.array(image)
    bgr_image = cv2.cvtColor(numpy_array, cv2.COLOR_RGB2BGR)
    gray = cv2.cvtColor(bgr_image, cv2.COLOR_BGR2GRAY)
    return gray
    
def fix_image(upload):
    image = Image.open(upload)
    col1.write("Original Image ::")
    col1.image(image)

    fixed = colourtobg(image)
    fixed_image = Image.fromarray(fixed)
    col2.write("Fixed Image :wrench:")
    col2.image(fixed_image)
    st.sidebar.markdown("\n")
    st.sidebar.download_button("Download fixed image", convert_image(fixed_image), "fixed.png", "image/png")



col1, col2 = st.columns(2)
my_upload = st.sidebar.file_uploader("Upload an image", type=["png", "jpg", "jpeg"])

if my_upload is not None:
    fix_image(upload=my_upload)

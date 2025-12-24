import streamlit as st
import numpy as np
from PIL import Image
import requests
from io import BytesIO
import matplotlib.pyplot as plt

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="Image Color Channel Visualizer",
    layout="wide"
)

# ---------------- TITLE ----------------
st.title("🖼️ Image Color Channel Visualizer")

# ---------------- LOAD IMAGE ----------------
@st.cache_data
def load_image():
    url = "https://media.vogue.co.uk/photos/68c14fa7250c555b5d7ad32f/2:3/w_1600,c_limit/Prada_25_Prototype_PR%20Portrait_8_16x9.jpg"
    response = requests.get(url)
    return Image.open(BytesIO(response.content)).convert("RGB")

# ---------------- DISPLAY ORIGINAL IMAGE ----------------
img = load_image()
st.image(img, caption="Original Image", width=800)

# ---------------- NUMPY CONVERSION ----------------
img_np = np.array(img)

R = img_np[:, :, 0]
G = img_np[:, :, 1]
B = img_np[:, :, 2]

# ---------------- CREATE CHANNEL IMAGES ----------------
red_img = np.zeros_like(img_np)
green_img = np.zeros_like(img_np)
blue_img = np.zeros_like(img_np)

red_img[:, :, 0] = R
green_img[:, :, 1] = G
blue_img[:, :, 2] = B

# ---------------- RGB CHANNEL DISPLAY ----------------
st.subheader("🎨 RGB Channel Visualization")

col1, col2, col3 = st.columns(3)

with col1:
    st.image(red_img, caption="Red Channel", width=300)

with col2:
    st.image(green_img, caption="Green Channel", width=300)

with col3:
    st.image(blue_img, caption="Blue Channel", width=300)

# ---------------- GRAYSCALE + COLORMAP ----------------
st.subheader("🌈 Colormapped Grayscale Image")

colormap = st.selectbox(
    "Choose a Matplotlib colormap",
    [
        "viridis", "plasma", "inferno",
        "magma", "cividis", "hot",
        "cool", "gray"
    ]
)

img_gray = img.convert("L")
img_gray_np = np.array(img_gray)

# ---------------- MATPLOTLIB DISPLAY ----------------
fig, ax = plt.subplots(figsize=(6, 4))
ax.imshow(img_gray_np, cmap=colormap)
ax.axis("off")

st.pyplot(fig)

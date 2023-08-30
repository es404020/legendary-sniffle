import cv2
import numpy as np
import streamlit as st


@st.cache_resource
def bw_filter(img):
    img_gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    return img_gray

@st.cache_resource
def sepia(img):
    img_sepia = img.copy()
    img_sepia = cv2.cvtColor(img_sepia, cv2.COLOR_BGR2RGB)
    img_sepia = np.array(img_sepia, dtype=np.float64)
    img_sepia = cv2.transform(img_sepia, np.matrix([
        [0.393, 0.769, 0.189],
        [0.349, 0.686, 0.168],
        [0.272, 0.534, 0.131]
    ]))
    img_sepia = np.clip(img_sepia, 0, 255)
    img_sepia = np.array(img_sepia, dtype=np.uint8)
    img_sepia = cv2.cvtColor(img_sepia, cv2.COLOR_RGB2BGR)

    return img_sepia

@st.cache_resource
def vignette(img, level=2):
    height, width = img.shape[:2]

    # Generate vignette mask using Gaussian kernels.
    X_resultant_kernel = cv2.getGaussianKernel(width, width / level)
    Y_resultant_kernel = cv2.getGaussianKernel(height, height / level)

    # Generating resultant_kernel matrix.
    kernel = Y_resultant_kernel * X_resultant_kernel.T
    mask = kernel / kernel.max()

    img_vignette = np.copy(img)

    # Applying the mask to each channel in the input image.
    for i in range(3):
        img_vignette[:, :, i] = img_vignette[:, :, i] * mask

    return img_vignette


@st.cache_resource
def embossed_edges(img):
    kernel = np.array([[0, -3, -3],
                       [3, 0, -3],
                       [3, 3, 0]])

    img_emboss = cv2.filter2D(img, -1, kernel=kernel)
    return img_emboss

@st.cache_resource
def bright(img, level):
    img_bright = cv2.convertScaleAbs(img, beta = level)
    return img_bright

@st.cache_resource
def outline(img, k=9):
    k = max(k, 9)
    kernel = np.array([[-1, -1, -1],
                       [-1, k, -1],
                       [-1, -1, -1]])

    img_outline = cv2.filter2D(img, ddepth=-1, kernel=kernel)

    return img_outline


@st.cache_resource
def pencile(img,ksize):
    img_blur = cv2.GaussianBlur(img, (ksize, ksize), 0, 0)
    img_sketch_bw, img_sketch_color = cv2.pencilSketch(img_blur)
    return  img_sketch_bw
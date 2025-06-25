import numpy as np
import cv2
from PIL import Image
import xml.etree.ElementTree as ET

# Function to apply Gaussian blur for image filtering
def apply_gaussian_blur(image, kernel_size=(5, 5)):
    numpy_image = np.array(image)
    blurred_image = cv2.GaussianBlur(numpy_image, kernel_size, 0)
    return Image.fromarray(blurred_image)

def process_image(jpg_file):
    target_size = (300, 300)
    image = Image.open(jpg_file)
    orig_size = image.size
    image = apply_gaussian_blur(image)
    image = image.resize(target_size, Image.ANTIALIAS)
    return image

import sys
sys.path.insert(0, './yolov7')

import torch
from yolov7.models.experimental import attempt_load
from yolov7.utils.general import non_max_suppression, scale_coords
from yolov7.utils.plots import plot_one_box
from PIL import Image
from torchvision.transforms import functional as F
import numpy as np
import os

# Load YOLOv7 model
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model = attempt_load("model.pkl", map_location=device)
model.eval()

# Define image processing function
def process_image(image):
    img = Image.open(image).convert("RGB")
    img = img.resize((640, 640))  # Resize input image to match model's input size
    img_tensor = F.to_tensor(img).unsqueeze(0).to(device)
    return img, img_tensor

# Define class names
class_names = {
    0: "Accident",
    1: "Non Accident"
}

# Define detection function
def detect_image(image_path):
    print("Detecting objects...")
    img, img_tensor = process_image(image_path)
    pred = model(img_tensor)[0]
    pred = non_max_suppression(pred, conf_thres=0.5, iou_thres=0.45)[0]
    class_detected = None

    if pred is not None:
        img_np = np.array(img)  # Convert PIL Image to NumPy array
        for *xyxy, conf, cls in pred:
            class_detected = class_names[int(cls)]  # Get class name based on class index
            plot_one_box(xyxy, img_np, label=class_detected, color=(0, 255, 0))
        
        img_result = Image.fromarray(img_np)  # Convert NumPy array back to PIL Image

        # Determine file name based on detected class
        if class_detected == "Accident":
            img_result.save("uploads/accident_result.png")
            return "accident_result.png"
        elif class_detected == "Non Accident":
            img_result.save("uploads/non_accident_result.png")
            return "non_accident_result.png"

    print("Detection complete.")
    return None
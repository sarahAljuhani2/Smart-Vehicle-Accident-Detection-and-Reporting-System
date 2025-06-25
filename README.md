# 🚗 Smart Vehicle Accident Detection and Reporting System

This project is a smart, AI-powered web system designed to automatically detect vehicle accidents from CCTV footage and generate detailed accident reports using advanced deep learning models and the ChatGPT-4 API.

---

##  Project Objective

To revolutionize the traditional manual accident reporting process used by authorities such as **Najm** and insurance companies by automating the detection and reporting of traffic accidents.

---

## ⚙️ Key Features

-  Detects vehicle accidents using CCTV images
-  Utilizes deep learning models: YOLOv7, SSD, Faster R-CNN, RetinaNet
-  Integrates GPT-4 API for automated report generation
-  User-friendly web interface built with Flask, HTML, and CSS
-  Reports include time, location, possible causes, recommendations, and more

---

## 📊 Model Performance Summary

| Model        | Type       | Speed        | Accuracy (mAP) |
|--------------|------------|--------------|----------------|
| YOLOv7       | One-stage  | ⚡ Fastest    | ✅ 94%         |
| SSD          | One-stage  | Fast         | 83%            |
| Faster R-CNN | Two-stage  | Moderate     | 82%            |
| RetinaNet    | One-stage  | Moderate     | 84%            |

---

## 📌 Deployment

The final system was deployed as a local web application that allows **General Department of Traffic** employees to upload CCTV images and receive an automatically generated accident report powered by GPT-4.

---

## 🧠 CRISP-DM Methodology Followed

1. **Business Understanding**  
2. **Data Collection & Preparation**  
3. **Modeling & Evaluation**  
4. **Deployment**

---

##  Technologies Used

- Python  
- Flask  
- HTML/CSS  
- YOLOv7, RetinaNet, Faster R-CNN, SSD  
- ChatGPT-4 API  
- LabelImg (for annotation)

---

## 📁 Project Structure

- `app.py`: Main Flask application  
- `object_detection.py`: Accident detection logic  
- `gpt.py`: GPT-based report generator  
- `uploads/`: Uploaded images  
- `static/`: CSS, images, and videos  
- `templates/`: HTML templates for UI  
- `model.pkl`: Trained YOLOv7 model  
- `.gitignore`: Ignoring unnecessary files (e.g., venv, model, logs)

---

##  How to Run

```bash
# 1. Clone the repo
git clone https://github.com/sarahAljuhani2/Smart-Vehicle-Accident-Detection-and-Reporting-System.git
cd Smart-Vehicle-Accident-Detection-and-Reporting-System

# 2. Create virtual environment
python -m venv nenv
# Activate:
# Windows: nenv\Scripts\activate
# macOS/Linux: source nenv/bin/activate

# 3. Install requirements
pip install -r requirements.txt

# 4. Add your OpenAI API key to `.env` file:
OPENAI_API_KEY=your_openai_key_here

# 5. Run the app
python app.py

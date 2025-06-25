from flask import Flask, render_template, request, redirect, url_for,send_file
import os
from werkzeug.utils import secure_filename

from preprocess import process_image
from object_detection import detect_image
from gpt import report_generate



app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/detect', methods=['POST'])
def object_detection():

    image = request.files.get('image')  # Use get() to avoid KeyError if 'image' is not in request.files

    if image:
        filename = secure_filename(image.filename)

        # preprocess
        image = process_image(image)
        image_path = os.path.join("./uploads", filename)
        image.save(image_path)

        # object detection
        result_image_path = detect_image(image_path)

        if result_image_path == "accident_result.png":
            return render_template('accident.html')
        elif result_image_path == "non_accident_result.png":
            return render_template('no-accident.html')
        
@app.route('/generate_report', methods=['GET'])
def generate_report():
    report_file = report_generate("uploads/accident_result.png")

    # Serve the generated DOCX file for download
    return send_file(report_file, as_attachment=True)


if __name__ == '__main__':
    app.run(debug=True)

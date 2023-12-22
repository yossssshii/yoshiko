import os
from flask import (
     Flask, 
     request, 
     render_template)
import cv2

from model import  calculate_dark_ratio, fill_dark_regions

UPLOAD_FOLDER='./static/images'

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_user_files():
    if request.method == 'POST':
        upload_file = request.files['upload_file']
        image_path = os.path.join(UPLOAD_FOLDER,upload_file.filename)
        upload_file.save(image_path)
        dark_ratio = calculate_dark_ratio(image_path)
        output_path = fill_dark_regions(image_path, threshold=120, border_color=(238, 104, 123), fill_color=(219, 112, 147, 255), border_thickness=4)
        
        return render_template('result.html', dark_ratio=dark_ratio, image_path=image_path, output_path=output_path)
    

if __name__ == "__main__":
    app.run(debug=True)
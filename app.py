import os
import requests
from flask import Flask, request, jsonify
from deepface import DeepFace
from face_verification_script import verify_faces
from color_detection import process_image_and_check_color

app = Flask(__name__)

def download_image(url, local_path):
    response = requests.get(url)
    with open(local_path, 'wb') as file:
        file.write(response.content)

@app.route('/process_images', methods=['POST'])
def process_images():
    data = request.json
    img1_url = data['img1_url']
    img2_url = data['img2_url']
    color_rgb = data['color_rgb']

    # Generate local paths for downloaded images
    img1_path = 'img1_downloaded.jpeg'
    img2_path = 'office_presence.jpeg'

    # Download the images
    download_image(img1_url, img1_path)
    download_image(img2_url, img2_path)

    try:
        # Perform face verification
        result = verify_faces(img1_path, img2_path)

        if result:
            color_result = process_image_and_check_color(img2_path, color_rgb, 30)
            return jsonify({'result': 'Faces verified', 'color_matched': color_result})
        else:
            return jsonify({'result': 'Faces not matched'})
    finally:
        # Clean up downloaded images
        os.remove(img1_path)
        os.remove(img2_path)

if __name__ == "__main__":
    app.run(debug=True)

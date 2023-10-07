from deepface import DeepFace
from PIL import Image
import requests
import tempfile
import os

def verify_faces(img1_url, img2_url):
    # Download the images from the URLs
    response1 = requests.get(img1_url)
    response2 = requests.get(img2_url)

    # Check if the requests were successful
    if response1.status_code == 200 and response2.status_code == 200:
        # Create temporary files to store the downloaded images
        with tempfile.NamedTemporaryFile(delete=False, suffix='.jpg') as img1_tempfile:
            img1_tempfile.write(response1.content)
            img1_path = img1_tempfile.name

        with tempfile.NamedTemporaryFile(delete=False, suffix='.jpg') as img2_tempfile:
            img2_tempfile.write(response2.content)
            img2_path = img2_tempfile.name

        # Load the images using PIL
        img1_pil = Image.open(img1_path)
        img2_pil = Image.open(img2_path)

        # Perform facial recognition with deep_face
        result = DeepFace.verify(img1_path=img1_path, img2_path=img2_path, model_name='VGG-Face')

        if result["verified"]:
            print("RESULT: Faces Matched!")
        else:
            print("RESULT: Faces Don't Match")

        # Delete the temporary files when done
        os.remove(img1_path)
        os.remove(img2_path)
    else:
        print("Failed to download one or both of the images from the URLs.")

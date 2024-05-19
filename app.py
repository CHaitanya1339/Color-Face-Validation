import os
import requests
from deepface import DeepFace
from face_verification_script import verify_faces
from color_detection import process_image_and_check_color

def download_image(url, local_path):
    response = requests.get(url)
    with open(local_path, 'wb') as file:
        file.write(response.content)

def main(img1_url, img2_url):
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
            print("The faces are verified, checking for color presence.")
            process_image_and_check_color(img2_path, (0,0,0), 30)
        else:
            print("The faces are not matched.")
    finally:
        # Clean up downloaded images
        os.remove(img1_path)
        os.remove(img2_path)

if __name__ == "__main__":
    img1_url = 'https://upload.wikimedia.org/wikipedia/commons/thumb/e/e6/Anushka_Sharma_promoting_Zero.jpg/220px-Anushka_Sharma_promoting_Zero.jpg'
    check_for_office_presence = 'https://1847884116.rsc.cdn77.org/hindi/gallery/actress/anushkasharma/nushkasharma281019_4.jpg'  

    main(img1_url, check_for_office_presence)

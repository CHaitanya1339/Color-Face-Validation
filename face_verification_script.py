from deepface import DeepFace

def verify_faces(img1_path, img2_path):
    # Perform facial recognition with DeepFace
    try:
        result = DeepFace.verify(img1_path=img1_path, img2_path=img2_path, model_name='VGG-Face', enforce_detection=False)
        return result["verified"]
    except ValueError as e:
        print(f"Error during verification: {e}")
        return False


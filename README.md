
# Image Processing and Face Verification Application

This application performs image processing tasks including face verification, color detection in images, and clothing segmentation. It is designed to handle tasks such as verifying if two faces in different images match, and checking for the presence of a specific color in clothing items within an image.

## Components

### 1. `app.py`
- **Description**: This is the main script that orchestrates the downloading of images, face verification, and color detection processes.
- **Key Functions**:
  - `download_image(url, local_path)`: Downloads an image from a URL to a local path.
  - `main(img1_url, img2_url)`: Main function to execute the face verification and color detection workflow.

### 2. `color_detection.py`
- **Description**: Contains functionality to process an image for color detection in specified clothing items.
- **Key Functions**:
  - `process_image_and_check_color(img_url, target_color_bgr, threshold_percentage)`: Processes an image to detect the presence of a specified color within the segmented clothing items.

### 3. `face_verification_script.py`
- **Description**: Provides face verification functionality using the DeepFace library.
- **Key Functions**:
  - `verify_faces(img1_path, img2_path)`: Verifies if two faces in different images match.

### 4. `SegCloth.py`
- **Description**: Handles the segmentation of clothing items in an image using a pre-trained model.
- **Key Functions**:
  - `segment_clothing(img, clothes=None)`: Segments specified clothing items from an image.

### 5. `requirements.txt`
- **Description**: Lists all the Python libraries that are required to run the application.
- **Libraries Included**:
  - Pillow
  - numpy
  - opencv-python
  - transformers
  - deepface
  - requests

## Installation

1. Clone the repository:

git clone <repository-url>

2. Install the required dependencies:

pip install -r requirements.txt


## Usage

Run the application by executing the `app.py` script:

python app.py


This will automatically download the images, perform face verification, and check for specific color presence in the clothing of the images.


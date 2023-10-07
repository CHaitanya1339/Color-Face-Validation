---
library: deepface
tags:
  - face-verification
  - deepface
  - vgg-face
---

 Model Name
Face Verification Model

## Description
This model performs face verification by comparing two images and determining if the faces match.

## Model Architecture
The model uses the VGG-Face architecture for facial recognition.

## Input
The model expects URLs of two images for face verification.

## Output
The output indicates whether the faces in the given images match or not.

## Usage
```python
from face_verification_script import verify_faces

# Example usage
result = verify_faces(img1_url='url_to_image1', img2_url='url_to_image2')
print(result)
```

# Dependencies
```bash
deepface==0.0.68
Pillow==8.3.2
```
# License
This model is released under the MIT License.

Limitations and Known Issues
The model may have limitations in certain lighting conditions.

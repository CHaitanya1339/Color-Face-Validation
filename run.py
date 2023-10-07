from face_verification_script import verify_faces

# URLs for the images you want to compare
img1_url = 'https://hamariweb.com/profiles/images/profile/7751-824-7085.jpg'
img2_url = 'https://hips.hearstapps.com/hmg-prod/images/gettyimages-693134468.jpg?crop=1xw:1.0xh;center,top&resize=1200:*'

# Example usage
result = verify_faces(img1_url, img2_url)
print(result)
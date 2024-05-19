from SegCloth import segment_clothing
from PIL import Image
import cv2
import numpy as np

def process_image_and_check_color(img_url, target_color_bgr, threshold_percentage):
    image = Image.open(img_url)
    result = segment_clothing(img=image, clothes=["Hat", "Upper-clothes", "Skirt", "Pants", "Dress", "Belt", "Left-shoe", "Right-shoe", "Scarf"])
    
    image_np = np.array(result.convert('RGB'))
    if image_np is None:
        raise ValueError("Image not found or path is incorrect")

    tolerance = 100
    lower_bound = np.array([max(0, target_color_bgr[0] - tolerance), max(0, target_color_bgr[1] - tolerance), max(0, target_color_bgr[2] - tolerance)])
    upper_bound = np.array([min(255, target_color_bgr[0] + tolerance), min(255, target_color_bgr[1] + tolerance), min(255, target_color_bgr[2] + tolerance)])

    color_mask = cv2.inRange(image_np, lower_bound, upper_bound)
    background_mask = cv2.inRange(image_np, (0, 0, 0), (254, 254, 254))
    final_mask = cv2.bitwise_and(color_mask, background_mask)

    total_pixels = image_np.size / 3
    target_pixels = np.sum(final_mask > 0)
    percentage = (target_pixels / total_pixels) * 100

    print(f"Percentage of target color in the image: {percentage:.2f}%")
    if percentage > threshold_percentage:
        print("The target color is present in more than 30% of the image.")
    else:
        print("The target color is not present in more than 30% of the image.")




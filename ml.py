import cv2
import pytesseract
import shutil


def identify_and_copy(image_path, keyword):
    img = cv2.imread(image_path)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    text = pytesseract.image_to_string(gray)

    if keyword in text:
        shutil.copy(image_path, "copied_images/")
        print("Image copied:", image_path)


# Example usage
image_path = "./gridcell_1.png"
keyword = "Inspire"
identify_and_copy(image_path, keyword)

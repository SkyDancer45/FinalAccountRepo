import img2pdf
from PIL import Image
import os

# storing image path
img_path = "../cow.png"


def get_png_files(directory):
    """Gets a list of all PNG file names in a given directory.

    Args:
      directory: The path to the directory to search.

    Returns:
      A list of PNG file names.
    """

    png_files = []
    for file in os.listdir(directory):
        if file.endswith(".png"):
            png_files.append(file)
    return png_files


# storing pdf path
pdf_path = "./file.pdf"

# opening image
image = Image.open(img_path)

# converting into chunks using img2pdf
pdf_bytes = img2pdf.convert(image.filename)

# opening or creating pdf file
file = open(pdf_path, "wb")

# writing pdf files with chunks
file.write(pdf_bytes)

# closing image file
image.close()

# closing pdf file
file.close()

# output
print("Successfully made pdf file")

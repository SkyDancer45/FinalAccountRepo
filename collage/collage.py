import os
import pypdf
import PyPDF2
from PIL import Image

# Specify the folder path containing your images
folder_path = "."

# Create a new PDF object
pdf_output = pypdf.PdfWriter()

# Iterate through images and add them to the PDF
for image_name in os.listdir(folder_path):
    if image_name.lower().endswith(('.jpg', '.jpeg', '.png')):  # Filter image formats
        image_path = os.path.join(folder_path, image_name)
        image = Image.open(image_path)

        # Convert image to RGB (if necessary)
        if image.mode != 'RGB':
            image = image.convert('RGB')

        # Create a new PDF page
        page = pypdf.generic.PdfObject()
        page.add_content(image.convert('RGB').tobytes())
        pdf_output.add_page(page)

# Save the PDF
with open("output.pdf", "wb") as output_file:
    pdf_output.write(output_file)

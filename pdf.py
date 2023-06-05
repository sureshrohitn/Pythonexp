import docx2pdf
from pdf2docx import Converter

"""Converting the Word Files into PDF files"""

docx2pdf.convert("C:/Users/CMR/Downloads/Certificates/", "C:/Users/CMR/Downloads/Certificates/pdf/")


"""
from wand.image import Image

file = 'C:/Users/CMR/Downloads/Certificates/pdf/Suresh N-CMRU-Webinar-Certificate.pdf'

with(Image(filename=file, resolution=300)) as img:
    images = img.sequence

    pages = len(images)
    for i in range(pages):
        images[i].type = 'grayscale'
        Image(images[i]).save(filename=str(i + 1) + '.png')
"""
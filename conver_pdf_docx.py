from pdf2docx import Converter
pdffile='Python.pdf'
docxfile='example.docx'
cv=Converter(pdffile)
cv.convert(docxfile)
cv.close()

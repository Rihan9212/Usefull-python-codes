from pdf2docx import Converter

pdf_file = "data-science-roadmap.pdf"
docx_file = "resume.docx"

cv = Converter(pdf_file)
cv.convert(docx_file)
cv.close()

print("converted to word document")
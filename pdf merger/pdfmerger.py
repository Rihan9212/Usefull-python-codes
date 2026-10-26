from pypdf import PdfWriter
import glob

merger = PdfWriter()

for pdf in sorted(glob.glob("*.pdf")):
    if pdf == "merged.pdf":
        continue
    merger.append(pdf)

merger.write("merged.pdf")
merger.close()

print("Merged pdf created successfully")
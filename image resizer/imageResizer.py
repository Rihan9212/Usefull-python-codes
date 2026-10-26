import os
from PIL import Image

folder = input("Folder Path: ")

os.makedirs("resized", exist_ok=True)

for filename in os.listdir(folder):
    if filename.lower().endswith((".jpg", ".jpeg", ".png")):
        img = Image.open(os.path.join(folder, filename))
        img = img.resize((800, 600))
        img.save(os.path.join("resized", filename))

print("All images resized")
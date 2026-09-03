import os
from PIL import Image

folder = "assets"
for filename in os.listdir(folder):
    if filename.lower().endswith(".jfif"):
        filepath = os.path.join(folder, filename)
        img = Image.open(filepath)
        new_name = filename.rsplit(".", 1)[0] + ".jpg"
        new_path = os.path.join(folder, new_name)
        img.convert("RGB").save(new_path, "JPEG")
        print(f"Converted: {filename} -> {new_name}")
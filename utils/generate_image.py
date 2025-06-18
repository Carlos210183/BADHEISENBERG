from PIL import Image, ImageDraw
import os

def generate_image(prompt):
    image_path = "/tmp/image.jpg"
    img = Image.new("RGB", (720, 1280), color=(73, 109, 137))
    d = ImageDraw.Draw(img)
    d.text((10, 10), prompt, fill=(255, 255, 0))
    img = img.resize((720, 1280), Image.LANCZOS)  # <- Esta es la forma correcta ahora
    img.save(image_path)
    return image_path
 Fix ImageResampling usando Image.LANCZOS

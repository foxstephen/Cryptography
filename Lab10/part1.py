from PIL import Image
import numpy as np

image = Image.open("flow.jpg")
width, height = image.size


pixels = []
for x in range(0, width):
  for y in range(0, height):
    pixels.append(image.getpixel((x, y)))

outImage.save("out.jpg", "JPEG")

    

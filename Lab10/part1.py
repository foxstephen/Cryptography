from PIL import Image
import numpy as np

image = Image.open("flow.jpg")
(width, height) = image.size

pixels = np.fromiter(iter(image.getdata()), np.uint8)
pixels.resize(height, width)
outImage = Image.fromarray(pixels, 'L')
outImage.save("out_part1.jpg", "JPEG")



    

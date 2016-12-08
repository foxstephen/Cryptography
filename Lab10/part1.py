from PIL import Image
import numpy as np

image = Image.open("baboon.bmp")
(width, height) = image.size

pixels = np.fromiter(iter(image.getdata()), np.uint8)
pixels.resize(height, width)
outImage = Image.fromarray(pixels, 'L')
image.save("out_part1.bmp")




    

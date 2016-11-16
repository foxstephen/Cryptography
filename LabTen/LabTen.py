import os,sys
import numpy as np
from PIL import Image
import bitstring
import hashlib


# Part 1
image = Image.open("doggy.jpg")


# Part 2
# print "Enter message"
# message = raw_input()

width, height = image.size

originalPixels = []
control = []
stegoPixels = []

 
messageCounter = {
  chars
  char: '',
  index: 2 # Start from index two as each bit is 0b10101011
}

for x in range(0, width):
  for y in range(0, height):
    pixel = image.getpixel((x, y)) # Keep original pixels
    originalPixels.append(pixel)
    control.append(pixel)

    pixelString = str(bin(pixel[0]))
    lsb = str(bin(ord('s')))[2] # The lsb for the current pixel

    # Pixel with lsb set to the correct bit of the message
    pixelWithLsb = pixelString[0:-1] + lsb

    # Convert the bit string with the correct lsb back to binary. 
    r = bitstring.Bits(pixelWithLsb)
    pixel = (r.uint, r.uint, r.uint)
    image.putpixel((x, y), pixel)

    stegoPixels.append(pixel) # Pixels with lsb changed.

      
  
image.save("out.jpg")
# hash outputs to show difference in original vs image with message.
print "Hash of original image" + hashlib.sha224(repr(originalPixels).encode('utf-8')).hexdigest()
print hashlib.sha224(repr(control).encode('utf-8')).hexdigest()
print "Hash of image with message encoded " + hashlib.sha224(repr(stegoPixels).encode('utf-8')).hexdigest()

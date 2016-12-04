import os,sys
import numpy as np
from PIL import Image
import bitstring
import hashlib



# Hashes of before and after image has had message hidden.,
hashes = {
  "originalPixels": [],
  "stegoPixels": []
}


# hides a message in a greyscale image
def hide(image, message):
  width, height = image.size

  # Each char of the message in binary with the '0b' part removed
  messageCharBits = map(lambda c: bin(ord(c))[2:], message)
  # Get all the bits that make up the message.
  messageBits = reduce(lambda prev, curr: prev + list(curr), messageCharBits, [])

  # Number of bits in the message
  messageBitCount = len(messageBits) 
  messageBitIndex = 0

  for x in range(0, width):
    for y in range(0, height):
      pixel = image.getpixel((x, y))
      hashes["originalPixels"].append(pixel)

      # Check if image has rgb values or is just white values.
      pixelToChange = pixel[0] if type(pixel) is tuple else pixel

      pixelAsBinary = bin(pixelToChange)
      if (messageBitIndex < messageBitCount):
        lsb = messageBits[messageBitIndex] # The new lsb to set on the current pixel from the message
        # Pixel with lsb set to the correct bit of the message
        pixelWithLsbSet = pixelAsBinary[0:-1] + lsb
        # Convert the binary string with the correct lsb back to binary. 
        r = bitstring.Bits(pixelWithLsbSet)

        # Check is origian pixel is rgb or white, and set the new pixel accordingly
        pixel = (r.uint, r.uint, r.uint) if type(pixel) is tuple else (r.uint) # new rgb or white value with with lsb set.
        image.putpixel((x, y), pixel)

        hashes["stegoPixels"].append(pixel) # Pixels with lsb changed.
        messageBitIndex += 1
      else: # Weve written the message no need to continue changing pixels.
        return

image = Image.open("flow.jpg")

print "Enter message: "
message = raw_input()
hide(image, message)

image.save("out.jpg")

# hash outputs to show difference in original vs image with message.
original = repr(hashes["originalPixels"])
hiddenMessage = repr(hashes["stegoPixels"])
print "original image hash :" + hashlib.sha224(original.encode('utf-8')).hexdigest()
print "hidden message hash :" + hashlib.sha224(hiddenMessage.encode('utf-8')).hexdigest()

print "Message hidden successfully in image!"
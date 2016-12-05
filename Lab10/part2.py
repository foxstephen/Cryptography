from PIL import Image

# generator for each bit in a message
def messageBitsGenerator(messageBits):
    i = 0
    while i < len(messageBits):
      yield messageBits[i]
      i += 1 

# Hide a message in the least significant bits of each pixel of an image
def hide(image, message):
  (width, height) = image.size # Get width and height of image.

  binMessage = ' '.join(format(ord(x), 'b') for x in message)

  bitsGenerator = messageBitsGenerator(binMessage) # Generator for each bit in message
  for x in range(0, width):
    for y in range(0, height):
      pixel = image.getpixel((x, y))

      if (image.mode is not 'L'): # Only support L mode as it is enough for grayscale
        print("This method does not support %s pixel models" % image.mode)
        return
      
      binPixel = bin(pixel)
      try:
        messageBit = bitsGenerator.next() # Get the current bit for the message
        binPixel = binPixel[:-1] + messageBit # Set the message bit as the LSB for the current pixel
        
        image.putpixel((x, y), int(binPixel, 2)) # Put pixel back into image at same coordinates.
      except StopIteration: 
        return # No more message bits to hide in image
      except ValueError as e:
        pass

image = Image.open("flow.jpg")
message = "Hello World!" * 600
hide(image, message)
image.save("hiddenMessage.jpg")
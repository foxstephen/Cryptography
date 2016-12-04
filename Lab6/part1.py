import os


# Create a one time pad that
# is same length as message.
def oneTimePad(plaintext):
	return map(lambda el: ord(el) % 26, os.urandom(len(plaintext))) 
	

# Returns the position of the character
# in the alphabet. (ignores case)
def alphaPos(char):
	return ord(char.lower()) - 97

def applyPad(pad, plaintext):
	ciphertext = ''
	for (index, padnum) in enumerate(pad):
		char = plaintext[index]
		charPos = alphaPos(char) # get position of char in real alphabet
		paddedChar = (padnum + charPos) % 26 # apply pad
		ciphertext += chr(paddedChar + 97) # put back into ascii
	return ciphertext

# Removes the pad from the ciphertext
# to retrieve the plaintext
def removePad(pad, ciphertext):
	plaintext = ''
	for (index, padnum) in enumerate(pad):
		char = ciphertext[index]
		charPos = alphaPos(char) # get position in real alphabet
		plainChar = (charPos - padnum) % 26 # removepad
		plaintext += chr(plainChar + 97)
	return plaintext

# Encrypt message
def encrypt(pad, plaintext):
	return applyPad(pad, plaintext)

# Decrypt message
def decrypt(pad, ciphertext):
	return removePad(pad, ciphertext)

message = "secretmessage"
pad = oneTimePad(message)

ciphertext = encrypt(pad, message)
plaintext = decrypt(pad, ciphertext)

print("Pad used:\t %s"% pad)
print("Message:\t %s" % message)
print("Ciphertext:\t %s" % ciphertext)
print("Plaintext:\t %s" % plaintext)



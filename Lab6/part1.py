from random import randint

# Create a one time pad that
# is same length as message.
def oneTimePad(plaintext):
	pad = []
	for c in plaintext:
		pad.append(randint(0, 25))
	return pad

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
# to retrieve the 
def removePad(pad, ciphertext):
	plaintext = ''
	for (index, padnum) in enumerate(pad):
		char = ciphertext[index]
		charPos = alphaPos(char) # get position in real alphabet
		plainChar = (charPos - padnum) % 26 # removepad
		plaintext += chr(plainChar + 97)
	return plaintext


message = "hello my name is stephen"
pad = oneTimePad(message)
ciphertext = applyPad(pad, message)
plaintext = removePad(pad, ciphertext)

print("Message:\t %s" % message)
print("Ciphertext:\t %s" % ciphertext)
print("Plaintext:\t %s" % plaintext)



#4 (E)  16 (Q)  13 (N)  21 (V)  25 (Z) (message + key) mod 26


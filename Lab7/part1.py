def hexdigest(data):
	return data.encode('hex')

# Pad data - block size 8
def pad(data):
  	length = 8 - (len(data) % 8)
  	data += "\x00" * (length)
  	return data

# Compress the block with DES - ECB Mode in Davies-Meyer mode
def compress(source, block):
	from Crypto.Cipher import DES
	ciphertext = DES.new(source, DES.MODE_ECB).encrypt(block) 
	return "".join(chr(ord(x) ^ ord(y)) for x, y in zip(source, ciphertext))  

# Hash a message
def hash(message):
	paddedMessage = pad(message)
	iv = "00000000"
	state = iv
	for x in range(0, len(paddedMessage), 8):
		block = paddedMessage[x: x + 8]
		state = compress(state, block)
	return state

# Prints a hexdigest of the hash
message = "AAAABBBBCCCCD"
print("Message:\t%s" % message)
print("Hashed :\t%s" % hexdigest(hash(message)))



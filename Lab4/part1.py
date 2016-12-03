from Crypto.Cipher import AES

def encrypt(aes, plaintext):
    return aes.encrypt(plaintext).encode("hex")

# Decrypt using AES, returning plaintext.
def decrypt(aes, ciphertext):
    return aes.decrypt(ciphertext.decode("hex"))

# PKCS7 Padding RFC 2315
def pkcs7pad(data, mode="pad"):
	if len(data) == 16: return
	if mode == "pad":
		length = 16 - (len(data) % 16)
		data += chr(length) * length
		return data
	elif mode == "remove":
		pad = ord(data[-1])
		return data[:-pad]

key = '1234567812345678'
plaintext = 'AAAABBBBCCCCDDDDAA'

print("Key: %s" % key)
print("Plaintext: %s" % plaintext)

paddedPlaintext = pkcs7pad(plaintext) # pad the plaintext
print("padded plaintext: %s" % repr(paddedPlaintext))

aes = AES.new(key, AES.MODE_ECB)
encrpyted = encrypt(aes, paddedPlaintext)

print("AES Encrypted: %s" % encrpyted)

aes = AES.new(key, AES.MODE_ECB)
decrypted = decrypt(aes, encrpyted)
decrypted = pkcs7pad(decrypted, mode="remove") # remove the padding
 
print("AES Decrypted: %s" % repr(decrypted))
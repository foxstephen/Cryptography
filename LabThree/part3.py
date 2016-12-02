from Crypto.Cipher import DES


# Encrypt using DES, returning ciphertext encoded in hexadecimal.
def encrypt(des, plaintext):
    return des.encrypt(plaintext).encode("hex")

# Decrypt using DES, returning plaintext.
def decrypt(des, ciphertext):
    return des.decrypt(ciphertext.decode("hex"))

# PKCS7 Padding RFC 2315
def pkcs7pad(data, mode="pad"):
	if mode == "pad":
		length = 8 - (len(data) % 8)
		data += chr(length) * length
		return data
	elif mode == "remove":
		pad = ord(data[-1])
		return data[:-pad]

key = "12345678"
plaintext = "AAAABBBBCCCC"
ciphertext = "19FF4637BB2FE77C81987E5CB99B66E2"

print("key: %s" % key)
print("plaintext: %s" % plaintext)

paddedPlaintext = pkcs7pad(plaintext) # pad the plaintext
print("padded plaintext: %s" % repr(paddedPlaintext))

des = DES.new(key, DES.MODE_ECB)
encrypted = encrypt(des, paddedPlaintext)
print('DES Encrypted: %s' % encrypted)

decrypted = decrypt(des, encrypted)
decrypted = pkcs7pad(decrypted, mode="remove") # remove the padding
 
print('DES Decrypted: %s' % repr(decrypted))

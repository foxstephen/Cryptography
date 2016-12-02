from Crypto.Cipher import AES

def encrypt(aes, plaintext):
    return aes.encrypt(plaintext).encode("hex")

# Decrypt using DES, returning plaintext.
def decrypt(aes, ciphertext):
    return aes.decrypt(ciphertext.decode("hex"))

# PKCS7 Padding RFC 2315
def pkcs7pad(data, mode="pad"):
	if len(data) == 16: return data
	if mode == "pad":
		length = 16 - (len(data) % 16)
		data += chr(length) * length
		return data
	elif mode == "remove":
		pad = ord(data[-1])
		return data[:-pad]


def bruteforce(ciphertext):
  file = open("dictionary.txt")
  words = file.readlines()
  file.close()

  for word in words:
    word = word.strip()
    paddedKey = pkcs7pad(word)
    aes = AES.new(paddedKey, AES.MODE_ECB)
    plaintext = decrypt(aes, ciphertext)
    plaintext = pkcs7pad(plaintext, mode="remove")
    print(plaintext)
    

ciphertext = "43d3215c92a75a1478fcf9cb950d20dba628062fe8b278c4c21d0ea8f7179f16"
bruteforce(ciphertext)

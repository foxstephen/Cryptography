from Crypto.Cipher import AES


# PKCS7 Padding RFC 2315
def pkcs7pad(data, mode="pad"):
	if mode == "pad":
		length = 8 - (len(data) % 8)
		data += chr(length) * length
		return data
	elif mode == "remove":
		pad = ord(data[-1])
		return data[:-pad]

key = '1234567812345678'
plaintext = 'AAAABBBBCCCCDD'
pText = padPlaintext(plaintext)
paddedPlaintext = 'AAAABBBBCCCCDDDDAA\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x0014'

aes = AES.new(key, AES.MODE_ECB)
encrpyted = aes.encrypt(pText).encode('hex')
print(key)
print(encrpyted)

aes = AES.new(key, AES.MODE_ECB)
decrypted = aes.decrypt(encrpyted.decode('hex'))
print("Decrypted: ", decrypted)




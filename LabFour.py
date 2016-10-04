from Crypto.Cipher import AES
import base64
import re



key = '1234567812345678'
plaintext = 'AAAABBBBCCCCDDDDAA'
paddedPlaintext = 'AAAABBBBCCCCDDDDAA\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x0014'

aes = AES.new(key, AES.MODE_ECB)
encrpyted = aes.encrypt(paddedPlaintext).encode('hex')
print(key)
print(encrpyted)

aes = AES.new(key, AES.MODE_ECB)
decrypted = aes.decrypt(encrpyted.decode('hex'))
print("Decrypted: ", decrypted)


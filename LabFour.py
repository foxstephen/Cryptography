from Crypto.Cipher import AES
import base64
import re

def padPlaintext(plainText):
    padAmount = 16 - (len(plaintext) % 16)  
        
    # To make space for final \x0000 
    padString = ''
    if padAmount > 16:
        padString += (padAmount - 2) * '\x00'
    elif padAmount < 16:
        padString += (padAmount - 1) * '\x00'
    padString += (str(padAmount))
    plainText += padString
    return plainText

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




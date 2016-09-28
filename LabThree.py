from Crypto.Cipher import DES
import base64
import re


# Encrypt using DES, returning ciphertext encoded in hexadecimal.
def encrypt(des, plaintext):
    return des.encrypt(plaintext).encode("hex")

# Decrypt using DES, returning plaintext.
def decrypt(des, ciphertext):
    return des.decrypt(ciphertext.decode("hex"))
    


# Q1
# DES.MODE_ECB
key = "12345678"
plaintext = "AAAABBBBAAAABBBB"

des = DES.new(key, DES.MODE_ECB)
encrypted = encrypt(des, plaintext)
print(encrypted)

cipertext = "19FF4637BB2FE77C19FF4637BB2FE77C"
decrypted = decrypt(des, cipertext)
print(decrypted)

print '\n'

# Q2.
# DES.MODE_CBC
key = "12345678"
iv = "00000000"
plaintext = "AAAABBBBAAAABBBB"
ciphertext = "AAC823F6BBE58F9EAF1FE0EB9CA7EB08"
des = DES.new(key, DES.MODE_CBC, iv)
encrypted = encrypt(des, plaintext)
print(encrypted)

decrypted = decrypt(des, ciphertext)
print(decrypted)


print('\n')

# Q3.

# Pads an 8 byte string.
def padPlaintext(plaintext):
    paddingLength = len(plaintext) % 8
    if paddingLength == 0: return

    padLengthString = "\x00\x000" + str(paddingLength)
    # Add the pad amount to the plain text
    plaintext += padLengthString
    return plaintext

# Removes padding from a string.
def removePadding(plaintext):
    padding = re.search(r'\d+$', plaintext)
    if padding is None:
        # no padding just return string
        return plaintext
    else:
        return plaintext[:-2]



key = "12345678"
plaintext = "AAAABBBBCCCC"
ciphertext = "19FF4637BB2FE77C81987E5CB99B66E2"

# Pad the plaintext, so we have correct multiple of 8.
paddedPlaintext = padPlaintext(plaintext)

des = DES.new(key, DES.MODE_ECB)
encrypted = encrypt(des, paddedPlaintext)
print(encrypted)

decrypted = decrypt(des, encrypted)

# Remove padding from the decrypted string if there was any.
decrypted = removePadding(decrypted)
print(decrypted)




    



    

    


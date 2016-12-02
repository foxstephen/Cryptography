from Crypto.Cipher import DES


# Encrypt using DES, returning ciphertext encoded in hexadecimal.
def encrypt(des, plaintext):
    return des.encrypt(plaintext).encode("hex")

# Decrypt using DES, returning plaintext.
def decrypt(des, ciphertext):
    return des.decrypt(ciphertext.decode("hex"))


key = "12345678"
plaintext = "AAAABBBBAAAABBBB"
cipertext = "19FF4637BB2FE77C19FF4637BB2FE77C"

print("key: %s" % key)
print("Plaintext: %s" % plaintext)

des = DES.new(key, DES.MODE_ECB)
encrypted = encrypt(des, plaintext)
print('DES.MODE_ECB Encrypted: %s' % encrypted)

decrypted = decrypt(des, cipertext)
print('DES.MODE_ECB Decrypted: %s' % decrypted)

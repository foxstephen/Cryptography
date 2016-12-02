from Crypto.Cipher import DES


# Encrypt using DES, returning ciphertext encoded in hexadecimal.
def encrypt(des, plaintext):
    return des.encrypt(plaintext).encode("hex")

# Decrypt using DES, returning plaintext.
def decrypt(des, ciphertext):
    return des.decrypt(ciphertext.decode("hex"))

# Q2.
# DES.MODE_CBC
key = "12345678"
iv = "00000000"
plaintext = "AAAABBBBAAAABBBB"
ciphertext = "AAC823F6BBE58F9EAF1FE0EB9CA7EB08"

print("key: %s" % key)
print("iv: %s" % iv)
print("Plaintext: %s" % plaintext)

des = DES.new(key, DES.MODE_CBC, iv)
encrypted = encrypt(des, plaintext)
print('DES.MODE_CBC Encrypted: %s' % encrypted)

des = DES.new(key, DES.MODE_CBC, iv)
decrypted = decrypt(des, ciphertext)
print('DES.MODE_CBC Decrypted: %s' % decrypted)
from Crypto.Cipher import AES

def encrypt(aes, plaintext):
    return aes.encrypt(plaintext).encode("hex")

# Decrypt using AES, returning plaintext.
def decrypt(aes, ciphertext):
    return aes.decrypt(ciphertext.decode("hex"))


# Attempts to brute force via dictionary attack.
def dictionaryAttack(ciphertext):
  file = open("dictionary.txt")
  words = file.readlines()
  file.close()

  for word in words:
    key = word.strip()
    aes = AES.new(key, AES.MODE_ECB)
    plaintext = decrypt(aes, ciphertext)
    print("%s decrypted plaintext: %s" % (key, plaintext))
    

ciphertext = "43d3215c92a75a1478fcf9cb950d20dba628062fe8b278c4c21d0ea8f7179f16"
dictionaryAttack(ciphertext)

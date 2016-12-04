import rsa # Module can be found here: https://stuvel.eu/python-rsa-doc/installation.html

# Generate private and public key
def genKeys(bitsize):
  return rsa.newkeys(bitsize)

# Encrypt with RSA.
def encrypt(message, pubKey):
  return rsa.encrypt(message, pubKey)

# Decrypt with RSA.
def decrypt(encrypted, privKey):
  return rsa.decrypt(encrypted, privKey)

(publicKey, privateKey) = genKeys(256)
message = "Hello Bob!"

encrypted = encrypt(message, publicKey)
decrypted = decrypt(encrypted, privateKey)

print("Alice wants to send Bob the message %s." % message)
print("Alice encrypts the message using Bob's public key: %s" % encrypted.encode('hex'))
print("Bob decrypts the message using his private key: %s." % decrypted)

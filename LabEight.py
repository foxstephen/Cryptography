# Part 1
p = 23
g = 5

a = 6
b = 15
aliceSecret = 0
bobSecret = 0
A = 0
B = 0
print("Alice and Bob agree on prime modulus p=%i and g=%i" % (p, g))
A = (g**a) % p
print("Alice chooses a=%i, then sends Bob A=%i" % (a, A))
B = (g**b) % p
print("Bob chooses a secret integer b=%i, then sends Alice B=%i" % (b, B))
aliceSecret = (B**a) % p
print("Alice computes secret=%i" % (aliceSecret))
bobSecret = (A**b) % p
print("Bob computes secret=%i" % (bobSecret))


# Funtion for Diffie-Hellman
def dhSecret(prime, base, a, b):
    A = (base**a) % prime
    B = (base**b) % prime
    aSecret = (B**a) % p
    bSecret = (A**b) % p
    if aSecret == bSecret:
        return (aSecret, bSecret)
print(dhSecret(p, g, a, b))


# Part 2
from Crypto.PublicKey import RSA
from Crypto import Random
import ast

random = Random.new().read
key = RSA.generate(1024, random)
publicKey = key.publickey()
encrypted = publicKey.encrypt("encrypt this message", 32)
print("Encrypted")
print(encrypted)

decrypted = key.decrypt(ast.literal_eval(str(encrypted)))
print("Decrypted")
print(decrypted)



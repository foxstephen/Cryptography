# Function check for Diffie-Hellman
def dhSecretCheck(prime, primitiveRoot, a, b):
    A = (primitiveRoot**a) % prime
    B = (primitiveRoot**b) % prime
    aSecret = (B**a) % p
    bSecret = (A**b) % p
    if aSecret == bSecret:
        return (aSecret, bSecret)


p = 23
g = 5

a = 6
b = 15
aliceSecret = 0
bobSecret = 0
A = 0
B = 0
print("Alice and Bob agree on prime modulus p=%i and primitive root g=%i" % (p, g))
A = (g**a) % p
print("Alice chooses a=%i, then sends Bob A=%i" % (a, A))
B = (g**b) % p
print("Bob chooses a secret integer b=%i, then sends Alice B=%i" % (b, B))
aliceSecret = (B**a) % p
print("Alice computes secret=%i" % (aliceSecret))
bobSecret = (A**b) % p
print("Bob computes secret=%i" % (bobSecret))




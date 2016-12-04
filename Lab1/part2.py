print "RAIL FENCE CIPHER"
def fence(p, k):
    fence = [[None] * len(p) for n in range(k)]
    rails = range(k - 1) + range(k - 1, 0, -1)
    for n, x in enumerate(p):
        fence[rails[n % len(rails)]][n] = x
    return [c for rail in fence for c in rail if c is not None]

def encryptRail(p, k):
    return ''.join(fence(p, k))

def decryptRail(c, k):
    rng = range(len(c))
    pos = fence(rng, k)
    return ''.join(c[pos.index(k)] for k in rng)

message = "Stephen Fox"
key = 3

# Encrypt message
encrypted = encryptRail(message, key)
print("Encrypted: %s to %s" %  (message, encrypted))

decrypted = decryptRail(encrypted, key)
print("Decrypted: %s to %s" %  (encrypted, decrypted))
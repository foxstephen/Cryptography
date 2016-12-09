

def gcd (a, b):
  if b == 0: 
    return a
  else: 
    return gcd(b, a % b)

# multiplicative inverse
def mmi(a, b):
  _a = a
  x = 0
  prevX = 1
  y = 1
  prevY = 0

  while b != 0:
    temp = b
    quotient = a/b
    b = a % b
    a = temp

    temp = x
    a = prevX - quotient * x
    prevX = temp

    temp = y
    y = prevY - quotient * y
    prevY = temp
  return _a + prevY


def generateKeys():
  p = 101
  q = 103
  n = p * q
  m = (p - 1) * (q - 1)
  e = 3

  while 1:
    if gcd(m, e) == 1: 
      break
    else: 
      e = e + 2
  
  d = mmi(m, e)
  return ((n,e), (n,d))


def encrypt(n, e, inputNum):
   return (inputNum ** e) % n
  
def decrypt(n, d, encrypted): 
   return (encrypted ** d) % n


publicKey, privateKey = generateKeys()
n, e = publicKey
n, d = privateKey

print("Generating public and private keys:")
print("Public key (n, e) " + str(publicKey))
print("Public key (n, d) " + str(privateKey))
print("n: %d e: %d" % (n, e))
print("n: %d d: %d" % (n, d))

numToEncrypt = 2001
encryptedNum = encrypt(n, e, numToEncrypt)
print("Encrypt %d to %d" % (numToEncrypt, encryptedNum))
print("Decrypt %d to %d" % (encryptedNum, decrypt(n, d, encryptedNum)))


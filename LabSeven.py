import base64
from Crypto.Cipher import DES
import hashlib
import hmac

# Part 1, hash function.
def addPadding(data):
    length =  8 - (len(data) % 8)
    data += "\x00" * (length)
    return data

def chunks(longdata, n):
    for i in range(8, len(longdata),n):
        yield longdata[i:i +n]

iv = '00000000'
plaintext = 'AAAABBBBCCCCD'
plaintextPadded = addPadding(plaintext)
datasource = dict(enumerate(list(chunks(plaintextPadded, 8)), start=0))

print str(datasource)

hash = iv
for d in datasource:
    des = DES.new(datasource[d], DES.MODE_ECB)
    cipherText = des.encrypt(hash)
    hash = "".join(chr(ord(x) ^ ord(y)) for x, y in zip(hash, cipherText))

print "plaintext: " + plaintext
print "hash "  + str(map("".join, zip(*[iter(base64.b16encode(hash))] * 16)))


# Part 2. MAC
import hashlib
import hmac

key = "TESTKEY1234"
message = "AAAABBBBCCCC"
result = hmac.new(key, message, hashlib.sha256).hexdigest()
# Compare the output of the two hashes with the key and message.
# If the message or key weren't the same the compare would return false.
print hmac.compare_digest(hmac.new(key, message, hashlib.sha256).hexdigest(), result)

print result
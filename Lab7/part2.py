# Part 2. MAC
import hashlib
import hmac

# Checks authenticity of message sent from a to b.
def checkMAC(sentDigest, receivedMessage, key):
  recieverDigest = hmac.new(key, receivedMessage, hashlib.md5).hexdigest()
  if hmac.compare_digest(sentDigest, recieverDigest):
    print("Original Message Digest: %s" % sentDigest)
    print("Incoming Message Digest: %s" % recieverDigest)
    print("Message OK, digests match.")
  else: 
    print("Original Message Digest: %s" % sentDigest)
    print("Incoming Message Digest: %s" % recieverDigest)
    print("Message BAD, WARNING: digests do not match.")


key = "TESTKEY1234"
originalMessage = "AAAABBBBCCCC"
incomingMessage = "AAAABBBBCCCC"

# Successful authentication code
print("Key used by both parties: %s" % key)
print("Original Message: %s" % originalMessage)
print("Incoming Message: %s" % incomingMessage)
originalMessageDigest = hmac.new(key, originalMessage, hashlib.md5).hexdigest()
checkMAC(originalMessageDigest, incomingMessage, key)


# Failed MAC by key change from "hacker"
hackerKey = "HACKERKEY1234"
print("\nKey used by sender: %s" % key)
print("Key used by hacker: %s" % hackerKey)
print("Original Message: %s" % originalMessage)
print("Incoming Message: %s" % incomingMessage)
# Check the MAC
checkMAC(originalMessageDigest, incomingMessage, hackerKey)

# Failed MAC by message change
hackedMessage = originalMessage + "D"  # append D on the end
print("\nKey used by both parties: %s" % key)
print("Original Message: %s" % originalMessage)
print("Incoming Message: %s" % hackedMessage)
checkMAC(originalMessageDigest, hackedMessage, key)






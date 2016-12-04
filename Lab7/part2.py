# Part 2. MAC
import hashlib
import hmac

key = "TESTKEY1234"
originalMessage = "AAAABBBBCCCC"
incomingMessage = "AAAABBBBCCCC"

# Successful authentication code
print("Key used: %s" % key)
print("Original Message: %s" % originalMessage)
print("Incoming Message: %s" % incomingMessage)

originalMessageDigest = hmac.new(key, originalMessage, hashlib.md5).hexdigest()
incomingMessageDigest = hmac.new(key, incomingMessage, hashlib.md5).hexdigest()
print("Original Message Digest: %s" % originalMessageDigest)
print("Incoming Message Digest: %s" % incomingMessageDigest)

if hmac.compare_digest(originalMessageDigest, incomingMessageDigest):
  print("Message OK, digests match.")
else: 
  print("Message BAD, WARNING: digests do not match.")


# Failed authentication code
hackerKey = "HACKERKEY1234"
hackedIncomingMessageDigest = hmac.new(hackerKey, incomingMessage, hashlib.md5).hexdigest()

print("\nKey used by sender: %s" % key)
print("Key used by hacker: %s" % hackerKey)
print("Original Message: %s" % originalMessage)
print("Incoming Message: %s" % incomingMessage)
if hmac.compare_digest(hackedIncomingMessageDigest, incomingMessageDigest):
  print("Message OK, digests match.")
else: 
  print("Message BAD, WARNING: digests do not match.")



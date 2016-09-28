
def caesar(s, k, decrypt=False):
    if decrypt: k = 26 - k
    r = ""
    for i in s:
        if (ord(i) >= 65 and ord(i) <= 90):
            r += chr((ord(i) - 65 + k) % 26 + 65)
        elif (ord(i) >= 97 and ord(i) <= 122):
            r += chr((ord(i) - 97 + k) % 26 + 97)
        else:
            r += i
    return r

def encrypt(p, k):
    return caesar(p, k)

def decrypt(c, k):
    return caesar(c, k, True)

plainText = '''
And I shall remain satisfied, and proud to have been the first who has ever enjoyed the fruit
of his writings as fully as he could desire; for my desire has been no other than to deliver
over to the detestation of mankind the false and foolish tales of the books of chivalry, which,
thanks to that of my true Don Quixote, are even now tottering, and doubtless doomed to fall
for ever. Farewell.
'''

# ***** PART 1
c = encrypt(plainText, -3)
print("Part 1")
print(c)

cipherText = '''
Vg jbhyq frrz gung, nf ur rknzvarq gur frireny cbffvovyvgvrf, n fhfcvpvba pebffrq uvf zvaq: gur zrzbel bs ubj ur 
uvzfrys unq orunirq va rneyvre qnlf znqr uvz nfx jurgure fbzrbar zvtug or uvqvat ure sebz gur jbeyq
'''

# ***** PART 2
# Instead of just using the value, you can brute force it using a forloop
# range 1..26 or -1 .. -26
p = decrypt(cipherText, 13)
print("Part 2")
print(p)


# PART 3
LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
myMessage = "Yhwvtroi, 28 Yudq 2016 - Pse bjatw pt foxgf zwjzql bgio qcwelwlar, blsg rmprochek ewrv nsoyr uvs ndcljebv rk pkium hy bef; sjr wutm vljg aybefl ds ydx mchf asx bojw lwfxx, aph fjsbntzaju kkwixit hvbduyzkik wme ylpzs gdrdv. wbu wme mmou olhtsajg wutm mmmzwxv lanebx ejipkt, obn dtzwn avq fnf xicgo lhg sns yxstuqfb oxs fakdsipjn qj uvs uxny zwjv gjskwusr pgoe zqbklsg, cre wt cdmw oafv lstgqqsfkie, lzam ydae eibgsn urge pvvlw ipxfadogafua oj zfs kr uvssg pgoaf; rqi odiewsxi tg ldszu kavlff oxs mgldsi dsd vs uvs oadwjo, we rupqwjhwyc tg lds gdxt cptc wx ihw xqhluj, ba wp oqdxny gj smhwy qgdogsdn, lzam nlql nmws poitwj wbu ptrg lbddsay"
myKey = 'FACEBOOKPASSWORD'

def vigenere(key, message, mode):
    translated = [] # stores the encrypted/decrypted message string
    keyIndex = 0
    key = key.upper()
    for symbol in message: # loop through each character in message
        num = LETTERS.find(symbol.upper())
        if num != -1: # -1 means symbol.upper() was not found in LETTERS
            if mode == 'encrypt':
                num += LETTERS.find(key[keyIndex]) # add if encrypting
            elif mode == 'decrypt':
                num -= LETTERS.find(key[keyIndex]) # subtract if decrypting
            num %= len(LETTERS) # handle the potential wrap-around
            # add the encrypted/decrypted symbol to the end of translated.
            if symbol.isupper():
                translated.append(LETTERS[num])
            elif symbol.islower():
                translated.append(LETTERS[num].lower())
            keyIndex += 1 # move to the next letter in the key
            if keyIndex == len(key):
                keyIndex = 0
        else:
            # The symbol was not in LETTERS, so add it to translated as is.
            translated.append(symbol)
    return ''.join(translated)


def encryptVigenere(key, message):
    return vigenere(key, message, 'encrypt')
def decryptVigenere(key, message):
    return vigenere(key, message, 'decrypt')

decrypted = decryptVigenere(myKey, myMessage)
print(decrypted)





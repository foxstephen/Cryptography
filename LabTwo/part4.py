from langdetect import detect

def vigenere(key, message, mode):
    LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    translated = []
    keyIndex = 0
    key = key.upper()
    for symbol in message:
        num = LETTERS.find(symbol.upper())
        if num != -1:
            if mode == 'encrypt':
                num += LETTERS.find(key[keyIndex])
            elif mode == 'decrypt':
                num -= LETTERS.find(key[keyIndex])
            num %= len(LETTERS)
            if symbol.isupper():
                translated.append(LETTERS[num])
            elif symbol.islower():
                translated.append(LETTERS[num].lower())
            keyIndex += 1 
            if keyIndex == len(key):
                keyIndex = 0
        else:
            translated.append(symbol)
    return ''.join(translated)

def encryptVigenere(key, message):
    return vigenere(key, message, 'encrypt')
def decryptVigenere(key, message):
    return vigenere(key, message, 'decrypt')



cipherText = "Yhwvtroi, 28 Yudq 2016 - Pse bjatw pt foxgf zwjzql bgio qcwelwlar, blsg rmprochek ewrv nsoyr uvs ndcljebv rk pkium hy bef; sjr wutm vljg aybefl ds ydx mchf asx bojw lwfxx, aph fjsbntzaju kkwixit hvbduyzkik wme ylpzs gdrdv. wbu wme mmou olhtsajg wutm mmmzwxv lanebx ejipkt, obn dtzwn avq fnf xicgo lhg sns yxstuqfb oxs fakdsipjn qj uvs uxny zwjv gjskwusr pgoe zqbklsg, cre wt cdmw oafv lstgqqsfkie, lzam ydae eibgsn urge pvvlw ipxfadogafua oj zfs kr uvssg pgoaf; rqi odiewsxi tg ldszu kavlff oxs mgldsi dsd vs uvs oadwjo, we rupqwjhwyc tg lds gdxt cptc wx ihw xqhluj, ba wp oqdxny gj smhwy qgdogsdn, lzam nlql nmws poitwj wbu ptrg lbddsay"

# Attempts to brute force the vigenere cipher
# through a dictionary attack.
def bruteforce():
  file = open('dictionary.txt')
  words = file.readlines()
  file.close()

  for word in words:
    word = word.strip()
    decrypted = decryptVigenere(word, cipherText)
    
    lang = detect(decrypted) 
    
    if (lang == 'en'):
      print("Possible detection, key is: %s (y/n):\n%s" % (word, decrypted))
      answer = raw_input()
      if (answer == "y"):
        return
      elif (answer == "n"):
        print("Continuing to decrypt...\n")
      else:
        return
    
bruteforce()
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

plaintext = '''I shall (from now on) select and take the ingots individually in my own yard, and I shall
exercise against yuo my right of rejection because you have treated me with contempt
'''

ciphertext = encryptVigenere("PASSWORD", plaintext)
print(ciphertext)
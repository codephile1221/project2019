import sys
import enchant #pip install pyenchant

def encrypt(text,key):
    enText  = ''
    for ch in text:
        if ord(ch) == 32:
            enText += ch
        else:
            enText += chr((ord(ch) - 65 + key)% 26 + 65)
    return enText
     
# text = input("Enter the text you want to encrypt:").upper()
# k = int(input("Enter the key:"))
# print(encrypt(text,k))

def decrypt(enText,key = 0):
    enText = enText.upper()
    def decryptingAlg(key):
        text = ''
        for ch in enText:
            if ord(ch) == 32:
                text += ch
            else:
                text += chr((ord(ch) - 65 - key) % 26 + 65)
        return text

    if key != 0:
        return decryptingAlg(key)
    else:
        d = enchant.Dict("en_US")
        decrypteds = [None] 
        for k in range(1, 26):
            text = decryptingAlg(k) # decrypted texxt
            words = text.split()
            for word in words:
                if d.check(word):
                    return {"decrypted text" :text, "key": k}
                else:
                    decrypteds.append(text)
        return decrypteds


# print(decrypt("HMNHPJS RZYYTS GJJK", 5))
    


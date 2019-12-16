import sys
import enchant  #( pip install pyenchant )
d = enchant.Dict("en_US")
# text = input("Enter the text you want to encrypt:").upper()
# k = int(input("Enter the key:"))
# '''hello encrypt xyz'''
# enText  = ''
# for ch in text:
#     if ord(ch) == 32:
#         enText += ch
#     else:
#         enText += chr((ord(ch) - 65 + k)% 26 + 65)
# print(f"The encrypted text of {text} is {enText}\n")



enText = input("Enter the text you want to decrypt:").upper()
for k in range(1,26):
    text = ''
    for ch in enText:
        if ord(ch) == 32:
            text += ch
        else:
            text += chr((ord(ch) - 65 - k) % 26 + 65)
    words = text.split()
    for word in words:
        if d.check(word):
            print(word)
            print("**********************************")
            print( f'''MATCH FOUND!!!
encrypted text = {enText}
decrypted text = {text}
key = {k}
**********************************''')
            sys.exit()
    else:
        print(f"The decrypted text of {enText} with key {k} is {text}")



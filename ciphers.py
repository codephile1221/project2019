from caesar import encrypt,decrypt
from playfair import playfairCipher
print("Choose a cipher:\n1) Caesar cipher\n2)Playfair cipher")
opt = input("->")
if opt == '1':
    print("Choose an option:\n1)Encrypt text\n2)Decrypt text")
    opt = input("->")
    if opt == '1':
        text = input("Enter the text you want to encrypt:")
        key = int(input("Enter a key (between 1-25):"))
        print(f"Encypted text is {encrypt(text,key)}")
    else:
        text = input("Enter the text you want to decrypt:")
        key = int(input("Enter the key (Enter 0 for bruteforce/if key is unknown):"))
        print(decrypt(text,key))
else:
    print("Choose an option:\n1)Encrypt text\n2)Decrypt text")
    opt = input("->")
    text = input("Enter text:")
    key = input("ENter the key (string):")
    print(f"result:{playfairCipher(text,key)}")
    

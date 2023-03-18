import hashlib

FoundOut = 0
input_hash = input("Insert the hashed password: ")
Pass_Doc = input("Insert dictionary: ")

try:
    Pass_File = open(Pass_Doc, 'r')
except:
    print("Error: " + Pass_Doc + " has not been found")

for Word in Pass_File:

    EncryptedWord = Word.encode('utf-8')
    HashedWord = hashlib.md5(EncryptedWord.strip())
    Digest = HashedWord.hexdigest()

    if Digest == input_hash:
        print("Password Found out!!! \n The Password is: " + Word)
        FoundOut = 1
        break

if not FoundOut:
    print("Password not found in file " + Pass_Doc)



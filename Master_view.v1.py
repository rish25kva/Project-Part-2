import os
from Crypto.Cipher import PKCS1_v1_5# variation of PKCS1
from Crypto.PublicKey import RSA
from Crypto import Random # Random number generator
from Crypto.Hash import SHA


def decrypt_valuables(f):
    try:
        print(str(f,'ascii'))
        print("Not encoded. Try again!")
    except UnicodeDecodeError:
        dsize = SHA.digest_size
        sentinel = Random.new().read(13+dsize) #Assuming the data length is 13
        key = RSA.importKey(open('private_keys').read())
        cipher = PKCS1_v1_5.new(key) # Creation of cipher object
        # Decryption of text
        decoded_text = cipher.decrypt(f, sentinel)
        digest = SHA.new(decoded_text[:-dsize]).digest()
        if digest==decoded_text[-dsize:]:
                decoded_text=decoded_text[:-dsize]
                decoded_text = str(f, 'ascii')
                print(decoded_text)
        else:
                print("Incorrect Encryption!")


if __name__ == "__main__": 
    fn = input("Which file in pastebot.net does the botnet master want to view? ")
    if not os.path.exists(os.path.join("pastebot.net", fn)):
        print("The given file doesn't exist on pastebot.net")
        os.exit(1)
    f = open(os.path.join("pastebot.net", fn), "rb").read()
    decrypt_valuables(f)

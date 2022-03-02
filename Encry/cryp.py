from cryptography.fernet import Fernet


def key_cre():
    key = Fernet.generate_key()

    #encryption is handeled in a different folder
    with open(key_file, 'wb') as filekey: 
        filekey.write(key)
def encrypt():
    key_cre()
    with open(key_file, 'rb') as filekey:
        key = filekey.read()

    fernet = Fernet(key)

    with open(Auth_file, 'rb') as file:
        original = file.read()
        
    encryp = fernet.encrypt(original)

    with open (Auth_file, 'wb') as encrypted:
        encrypted.write(encryp)

def decryp():

    with open(key_file, 'rb') as filekey:
        key = filekey.read()
    fernet = Fernet(key)
   
    with open(Auth_file, 'rb') as encrypted_file:
        encrypted = encrypted_file.read()
    decrypted = fernet.decrypt(encrypted)

    with open(Auth_file, 'wb') as decrypted_file:
        decrypted_file.write(decrypted)
        
    return Auth_file


key_file = 'xxxxxxxx'  #replace xxxxxxxx with path to encryption file name, give it a .key extension
Auth_file = 'xxxxxxxx'          #replace xxxxxxxx with path to file containing authentication numbers
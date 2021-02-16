from cryptography.fernet import Fernet
# key=Fernet.generate_key()
# print(key)
# file=open('key.key','wb')
# file.write(key)
# file.close()
def generate_key():
    key=Fernet.generate_key()
    print(key)
    with open ('mykey.key','wb') as mykey:
        mykey.write(key)

def load_key():
    with open ('mykey.key','rb') as mykey:
        key = mykey.read()
        return key

def encrypt_file(filename):
    key=load_key()
    f=Fernet(key)
    with open(filename,'rb') as original_file:
        original = original_file.read()
    enc_file='enc'+str(filename)
    encryptol=f.encrypt(original)
    with open(enc_file,'wb') as encrypted_file:
        encrypted_file.write(encryptol)
    print('file is encrypted and save as'+ enc_file)
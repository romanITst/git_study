#! /usr/bin/env python3


from cryptography.fernet import Fernet

path_to_key = str(input("Enter the path to cryptography key: "))
with open(f"{path_to_key}", "rb") as path_to_key:
    key = path_to_key.read()

decipher = Fernet(key) #decipher function

encrypted_file = str(input("Enter the path to file you want to decrypt: "))
with open(f"{encrypted_file}", "rb") as encrypted_file:
    encrypted_data = encrypted_file.read()

decrypted_data = decipher.decrypt(encrypted_data)

decrypted_file = str(input("Enter the path you want to save the decrypted file: ")) 
with open(f"{decrypted_file}", "wb") as decrypted_file:
    decrypted_file.write(decrypted_data)
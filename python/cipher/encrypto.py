#! /usr/bin/env python3

#  Task description 
#  Зашифровать файл

from cryptography.fernet import Fernet  #Fernet - тип аутентифицированного шифрования

key = Fernet.generate_key()  #key generation
key_file = str(input("Enter the path to file you to save the cryptography key: "))
with open(f"{key_file}", "wb") as key_file:
    key_file.write(key)

cipher = Fernet(key)  #cipher function

file = str(input("Enter the path to file you want to encrypt: "))
with open(f"{file}", "rb") as file:
    data = file.read()

encrypted_data = cipher.encrypt(data)

encrypted_file = str(input("Enter the path you want to save the encrypted file: "))
with open(f"{encrypted_file}", "wb") as encrypted_file:
    encrypted_file.write(encrypted_data)
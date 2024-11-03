#! /usr/bin/env python3

#  Task description: Зашифровать файл.

from cryptography.fernet import Fernet

key = Fernet.generate_key()

cipher = Fernet(key)

with open("./file.txt", "rb") as file:
    data = file.read()
    encrypted_data = cipher.encrypt(data)


with open("./encrypted_file.txt", "wb") as file:
    file.write(encrypted_data)
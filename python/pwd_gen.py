#! /usr/bin/env python3

#task description: написать генератор пароля

import random

password = "abcdefghijklopqrstuvwxyz!@#$%^&*()_+".join("ABCDEFGHIJKLOPQRSTUVWXYZ123215498712936789213")
password_length = int(input("Enter the length of the password: "))

a = "".join(random.sample(password,password_length))

print(f"Your password is: {a} \nSave it in safe place and dont show anybody!")
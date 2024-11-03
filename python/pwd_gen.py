#! /usr/bin/env python3

#  Task description: написать генератор пароля

import random

password_pattern = "abcdefghijklmnopqrstuvwxyz".join("ABCDEFGHIJKLMNOPQRSTUVWXYZ").join("123215498712936789213").join("!@#$%^&*()_+|\/<>,.")
password_length = int(input("Enter the length of the password: "))

password = "".join(random.sample(password_pattern, password_length))

print(f"Your password is: {password} \nKeep it in a safe place and don't show it to anyone!")
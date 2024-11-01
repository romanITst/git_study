#! /usr/bin/env python3

word1 = str(input("Enter the word: "))
letter1 = str(input("Enter the letter you want to change in the word: "))
letter2 = str(input(f"Enter the letter you want to replace with the {letter1} in the word: "))
word2 = word1.replace(f"{letter1}", f"{letter2}")
print(f"The result is: {word2}")

#import random
#
#password = "abcdefghijklopqrstuvwxyz!@#$%^&*()_+".join("ABCDEFGHIJKLOPQRSTUVWXYZ123215498712936789213")
#password_length = int(input("Enter the length of the password: "))
#
#a = "".join(random.sample(password,password_length))
#
#print(f"Your password is: {a} \nSave it in safe place and dont show anybody!")
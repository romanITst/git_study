#! /usr/bin/env python3

#task description: написать скрипт заменяющий одну букву на другую в слове

word1 = str(input("Enter the word: "))
letter1 = str(input("Enter the letter you want to change in the word: "))
letter2 = str(input(f"Enter the letter you want to replace with the {letter1} in the word: "))
word2 = word1.replace(f"{letter1}", f"{letter2}")
print(f"The result is: {word2}")
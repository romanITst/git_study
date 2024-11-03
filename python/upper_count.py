#! /usr/bin/env python3

#  Пользователь вводит строку из букв и специальных
#  символов в нижнем регистре и верхнем регистре.
#  Нужно посчитать, сколько в этой строке больших букв.

print("Enter the string upper and lower case letters and special characters.")
input = input("The script will count the number of upper case letters: ")

count = 0

for I in input:
    if I.isupper():
        count += 1

print(f"The count of upper case letters is {count}")
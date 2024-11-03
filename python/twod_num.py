#! /usr/bin/env python3

#  Task description 
#  Посчитать сумму цифр двузначного числа, введённого с клавиатуры. (пока можно сколько угодно-значного)

twod_number = input("Enter the two-digit number: ")
digits_summ = 0

for num in twod_number:
    digits_summ += int(num)

print(digits_summ)
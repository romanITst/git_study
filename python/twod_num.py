#! /usr/bin/env python3

#task description: посчитать сумму цифр двузначного числа введённого с клавиатуры

twod_number = input("Enter the two-digit number: ")
digits_summ  = 0
for num in twod_number:
    digits_summ += int(num)
print(digits_summ)
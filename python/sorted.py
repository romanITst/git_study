#! /usr/bin/env python3

# Task description: отсортировать данный массив из чисел

numbers = [1, 3, 5, 2, 0, 75, 71, 69, 68, 34, 23, 99]
print(sorted(numbers))

# +вывести числа меньше определённого (допустим 5)
less_numbers = []
for num in numbers:
    if num < 5:
        less_numbers.append(num)
    
print(sorted(less_numbers))

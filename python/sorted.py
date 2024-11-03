#! /usr/bin/env python3

##task description: отсортировать данный массив из чисел

numbers = [1, 3, 5, 2, 0, 75, 71, 69, 68, 34, 23, 99]
print(sorted(numbers))
# + вывести числа меньше определённого
for num in numbers:
    if num < 5:
        print(num)
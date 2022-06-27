# Даны два целых числа.
# Вывести список всех чисел кратных трем в диапазоне между заданными числами.

first_number = int(input())     # Первое число
second_number = int(input())    # Второе число

# TODO: your code here
first_number = int(input("first number: "))     # Первое число
second_number = int(input("second number: "))    # Второе число
number = 0
if first_number < second_number:
    for number in range(first_number, second_number):
        if number % 3 == 0:
            print(number, end = " ")
if second_number < first_number:
    for number in range(second_number, first_number):
        if number % 3 == 0:
            print(number, end = " ")
            

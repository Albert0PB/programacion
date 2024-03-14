"""
The program asks for 10 numbers and gives them back in reverse.

Author: Alberto Pérez Bernabeu

Starting date: 13-11-23
Last modification: 13-11-23
"""

numbers_list = []
for n in range(10):
    number = input("Introduzca un número: ")
    numbers_list += number
print(f"{numbers_list[::-1]}")

"""
A program that checks if a String contains a Substring. Both are asked to user to input.

Author: Alberto Pérez Bernabeu

Starting date: 09-11-23
Last modification:
"""
from sys import exit

print("\nEste programa le permite comprobar si una subcadena se encuentra dentro de una cadena.")
print("--------------------------------------------------------------------------------------\n")

string = str(input("Introduzca una cadena:\n"))
substring = str(input("Introduzca una subcadena:\n"))

string_char = 0
substring_char = 0
total_char_string = 0
total_char_substring = len(substring)

"""
while substring_char != total_char_substring:
    if substring[substring_char] in string:
        substring_char += 1
    else:
        print(f"{substring} no está en {string}.")
        exit()
print(f"{substring} está en {string}.")
"""

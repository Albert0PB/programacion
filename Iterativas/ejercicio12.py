"""
Pide una cadena y dos caracteres por teclado (valida que sea un carácter), sustituye la aparición del
primer carácter en la cadena por el segundo carácter.

Author: Alberto Pérez Bernabeu

Starting date: 09-11-23
Last modification:
"""

string = str(input("Introduzca una cadena:\n"))

char_in_string = str(input("Introduzca un carácter a sustituir:\n"))
substitute_char = str(input("Introduzca el carácter sustituto:\n"))

for c in string:
    if c == char_in_string:
        string -= c
        string += substitute_char


"""
This program asks for a real (base) number and a positive integer (exponent) number and, without using the function nor
the operator in code, shows the result of the power.

Author: Alberto Pérez Bernabeu

Starting date: 28-10-23
Last modification: 01-11-23
"""

print("Este programa te ayuda a calcular el resultado de una potencia. Para ello, tendrás que introducir "
      "la base y el exponente.")

base = input("Introduzca la base, que puede ser cualquier número real:\n")

while True:
    if base.isalpha():
        base = input("¡Error! Asegúrese de introducir un número real como base.\n")
    else:
        break

exponent = input("Introduzca el exponente, que debe ser un entero positivo.\n")

while True:
    if exponent.isnumeric():
        break
    else:
        exponent = input("¡Error! Asegúrese de introducir un entero positivo como exponente.\n")


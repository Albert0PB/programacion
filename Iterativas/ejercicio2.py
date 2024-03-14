"""
A program that asks for a quantity of numbers decided by the user and tells how many of them are
lower, greater and equal to 0.

Author: Alberto Pérez Bernabeu

Starting date: 28-10-23
Last modification: 30-10-23
"""

from sys import exit

print("¡Bienvenido! En este programa determinas una cantidad de números a introducir y, una vez escribas todos los "
      "números, se indicará la cantidad de éstos que son mayores, menores e iguales a 0.\n")

number = 0
zero_counter = 0
lower_counter = 0
greater_counter = 0
quantity = 0

while quantity <= 0:
    quantity = int(input("Indique la cantidad de números que se dispone a introducir; este debe ser un numero "
                         "natural.\n"))

while quantity != 0:
    number = int(input("Introduzca un número.\n"))
    if number == 0:
        zero_counter += 1
    if number < 0:
        lower_counter += 1
    if number > 0:
        greater_counter += 1
    quantity -= 1

print(f"La cantidad de números introducidos iguales a cero asciende a {zero_counter}.")
print(f"La cantidad de números introducidos menores que cero asciende a {lower_counter}.")
print(f"La cantidad de números introducidos mayores que cero asciende a {greater_counter}.")

exit()

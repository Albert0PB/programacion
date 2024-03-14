"""
Program that shows all the even numbers between two limits defined by user.

Author: Alberto Pérez Bernabeu

Starting date: 28-10-23
Last modification: 30-10-23
"""

from sys import exit

print("Introduzca dos límites, y el programa mostrará todos los pares entre ellos.")

while True:
    print("Por favor, asegúrese de que el límite inferior es menor que el límite superior.\n")
    lower_limit = int(input("Introduzca el límite inferior.\n"))
    upper_limit = int(input("Introduzca el límite superior.\n"))
    if lower_limit < upper_limit:
        break

print(f"Estos son los pares entre {lower_limit} y {upper_limit}:\n")

for number in range(lower_limit, upper_limit):
    if number % 2 == 0:
        print(number)
exit()

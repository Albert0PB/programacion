"""
A game that consists in guessing a randomly generated number.

Author: Alberto Pérez Bernabeu

Starting date: 28-10-23
Last modification: 30-10-23
"""

from random import randint
from sys import exit
print("Intenta adivinar un número entre el 1 y el 100. Tienes diez intentos.")

random_number = randint(1, 100)
guess = int(input("Introduce el número que creas:\n"))
tries = 0

while tries < 10:
    if guess < random_number:
        guess = int(input("¡Error! El número es más alto; ¡sigue intentándolo!\n"))
    if guess > random_number:
        guess = int(input("¡Error! El número es más bajo; ¡sigue intentándolo!\n"))
    if guess == random_number:
        print(f"¡Enhorabuena, has acertado! Has necesitado {tries} intentos.")
    tries += 1
print(f"¡Te has quedado sin intentos! El número era {random_number}")

exit()

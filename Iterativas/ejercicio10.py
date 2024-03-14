"""
The program asks for a string and a character and tells how many times that character
is repeated in the string.

Author: Alberto Pérez Bernabeu

Starting date: 09-11-23
Last modification: 09-11-23
"""

string = input(str("Introduce tu cadena: \n"))

while True:
    char = str(input("Introduce un sólo carácter:\n"))
    if len(char) == 1:
        break

coincidences_counter = 0

for c in string:
    if c == char:
        coincidences_counter += 1

print(f"{char} se repite {coincidences_counter} veces en {string}.")

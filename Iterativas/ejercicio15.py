"""Program that checks if a string is a palindrome

Author: Alberto Pérez Bernabeu

Starting date: 09-11-23
Last modification: 09-11-23
"""

print("\nEste programa comprueba si la cadena que introduzca es un palíndromo.")
print("---------------------------------------------------------------------\n")

string = str(input("Introduzca su cadena:\n"))
half = round(int(len(string) / 2))

first_half = string[0:half]

if len(string) % 2 == 0:
    second_half = string[half:(half * 2)]
else:
    second_half = string[(half+1):((half+1) * 2)]
second_half_reversed = second_half[::-1]

if first_half == second_half_reversed:
    print(f"{string} es un palíndromo.")
else:
    print(f"{string} no es un palíndromo.")

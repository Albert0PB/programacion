"""
Escribe un programa que pida 10 números por teclado y que luego muestre los números introducidos junto con las palabras
“máximo” y “mínimo” al lado del máximo y del mínimo respectivamente.

Author: Alberto Pérez Bernabeu

Starting date: 19-11-2023
Last modification:
"""

numbers = []

for _ in range(0, 10):
    while True:
        try:
            numbers += [int(input("Introduzca un número: "))]
        except ValueError:
            print("Asegúrese de introducir un número.")
        break

print("\nNÚMEROS\n-------")

for number in numbers:
    if number == max(numbers):
        print(f"{number:^7} es el máximo en el array.")
    elif number == min(numbers):
        print(f"{number:^7} es el mínimo en el array.")
    else:
        print(f"{number:^7}")

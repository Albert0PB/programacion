"""
Escribe un programa que lea 15 números por teclado y que los almacene en un array. Rota los elementos de ese array, es
decir, el elemento de la posición 0 debe pasar a la posición 1, el de la 1 a la 2, etc. El número que se encuentra en
la última posición debe pasar a la posición 0. Finalmente, muestra el contenido del array.

Author: Alberto Pérez Bernabeu

Starting date: 19-11-2023
Last modification:
"""
from random import randrange

TOTAL_NUMBERS = 15

numbers_array = []

"""
for _ in range(TOTAL_NUMBERS):
    numbers_array.append(randrange(-1000, 1001))
print(numbers_array)
"""
for _ in range(TOTAL_NUMBERS):
    while True:
        try:
            numbers_array.append(float(input("Introduzca un número:\n")))
            break
        except ValueError:
            print("Asegúrese de introducir un número (se admiten decimales.")

array_copy = numbers_array.copy()
last_holder = numbers_array[len(numbers_array) - 1]

for _ in range(TOTAL_NUMBERS - 1):
    numbers_array[_ + 1] = array_copy[_]
numbers_array[0] = last_holder
print(numbers_array)

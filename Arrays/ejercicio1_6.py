"""
Escribe un programa que genere 20 números enteros aleatorios entre 0 y 100 y que los almacene en un array. El programa
debe ser capaz de pasar todos los números pares a las primeras posiciones del array (del 0 en adelante) y todos los
números impares a las celdas restantes. Utiliza arrays auxiliares si es necesario.

Author: Alberto Pérez Bernabeu

Starting date: 19-11-2023
Last modification: 20-11-2023
"""
from random import randrange

print("\nEste programa genera 20 números aleatorios y los expone, diferenciados en pares e impares, y ordenados de "
      "menor a mayor.\n")

random_list = [randrange(0, 100) for _ in range(0, 20)]
even_numbers_sublist = []
odd_numbers_sublist = []

for current_position_in_list in range(0, len(random_list)):
    if random_list[current_position_in_list] % 2 == 0:
        even_numbers_sublist += [random_list[current_position_in_list]]
    else:
        odd_numbers_sublist += [random_list[current_position_in_list]]

for _ in range(0, len(odd_numbers_sublist)):
    for position_in_odd_list in range(0, len(odd_numbers_sublist) - 1):
        if odd_numbers_sublist[position_in_odd_list] > odd_numbers_sublist[position_in_odd_list + 1]:
            odd_holder = odd_numbers_sublist[position_in_odd_list]
            odd_numbers_sublist[position_in_odd_list] = odd_numbers_sublist[position_in_odd_list + 1]
            odd_numbers_sublist[position_in_odd_list + 1] = odd_holder

for _ in range(0, len(even_numbers_sublist)):
    for position_in_even_list in range(0, len(even_numbers_sublist) - 1):
        if even_numbers_sublist[position_in_even_list] > even_numbers_sublist[position_in_even_list + 1]:
            even_holder = even_numbers_sublist[position_in_even_list]
            even_numbers_sublist[position_in_even_list] = even_numbers_sublist[position_in_even_list + 1]
            even_numbers_sublist[position_in_even_list + 1] = even_holder

output_list = even_numbers_sublist + odd_numbers_sublist

print(f"Lista generada aleatoriamente:\n{random_list}\n")
print(f"Lista con los números generados que son impares:\n{odd_numbers_sublist}\n")
print(f"Lista con los números generados que son pares:\n{even_numbers_sublist}\n")
print(f"Lista con pares e impares separados en dos secciones (los pares primero), ordenados de mayor a menor:\n" 
      f"{output_list}")


"""
NO HAY QUE ORDENAR DE MENOR A MAYOR PARES E IMPARES
"""
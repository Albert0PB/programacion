"""
Escribe un programa que pida 20 números enteros. Estos números se deben introducir en un array de 4 filas por 5
columnas. El programa mostrará las sumas parciales de filas y columnas igual que si de una hoja de cálculo se tratara.
La suma total debe aparecer en la esquina inferior derecha.

Author: Alberto Pérez Bernabeu

Starting date: 21-11-2023
Last modification: 21-11-2023
"""
from random import randrange

ROWS = 4
COLUMNS = 5

matrix = []


for _ in range(ROWS):   # a efectos de las pruebas
    row = [randrange(-1000, 1001) for _ in range(COLUMNS)]
    matrix.append(row)
"""
for _ in range(ROWS):
    while True:
        try:
            row = [int(input("Introduzca un número entero:\n")) for _ in range(COLUMNS)]
            matrix.append(row)
            break
        except ValueError:
            print("Asegúrese de introducir un número entero.")
"""

rows_subtotal = []
columns_subtotal = []

for j in range(COLUMNS):
    column_addition = 0
    for i in range(ROWS):
        column_addition += matrix[i][j]
    columns_subtotal.append(column_addition)

for i in range(ROWS):
    row_addition = 0
    for j in range(COLUMNS):
        row_addition += matrix[i][j]
    rows_subtotal.append(row_addition)

total_sum = 0
for n in range(ROWS):
    total_sum += rows_subtotal[n]

for r in range(ROWS):
    print(f"{matrix[r][0]:^5d} | {matrix[r][1]:^5d} | {matrix[r][2]:^5d} | {matrix[r][3]:^5d} | {matrix[r][4]:^5d} |"
          f"{rows_subtotal[r]:^8d}")
print("---------------------------------------")
print(f"{columns_subtotal[0]:^5d} | {columns_subtotal[1]:^5d} | {columns_subtotal[2]:^5d} | {columns_subtotal[3]:^5d} |"
      f" {columns_subtotal[4]:^6d}| {total_sum:^7d}")

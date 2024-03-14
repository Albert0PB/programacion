"""
Realiza un programa que rellene un array de 6 filas por 10 columnas con números enteros positivos comprendidos entre 0
y 1000 (ambos incluidos). A continuación, el programa deberá dar la posición tanto del máximo como del mínimo.

Author: Alberto Pérez Bernabeu

Starting date: 21-11-2023
Last modification:
"""
from random import randrange

ROWS = 6
COLUMNS = 10

matrix = []
for _ in range(ROWS):
    row = [randrange(0, 1001) for _ in range(COLUMNS)]
    matrix.append(row)

i_max = 0
j_max = 0
i_min = 0
j_min = 0

print("\n")
for i in range(ROWS):
    print(f" Fila {(i + 1)}  ", end="||")
    for j in range(COLUMNS):
        print(f"{matrix[i][j]:^9d}", end="|")
        if j == (COLUMNS - 1):
            print("\n")

print(f"Columnas", "||", end="")
for j in range(COLUMNS):
    print(f"{(j + 1):^9}", end="|")

print(f"\n\n El  valor máximo de la matriz se encuentra en la posición {i_max, j_max} y el valor mínimo en la posición "
      f"{i_min, j_min}.")

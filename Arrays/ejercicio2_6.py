"""
Realiza un programa que calcule la estatura media, mínima y máxima en centímetros de personas de diferentes países.
El array que contiene los nombres de los países es el siguiente:

paises = [“España”, “Rusia”, “Japón”, “Australia”]

Los datos sobre las estaturas se deben simular mediante un array de 4 filas por 10 columnas con números aleatorios
generados al azar entre 140 y 210. Los decimales de la media se pueden despreciar. Los nombres de los países se deben
mostrar utilizando el array de países (no se pueden escribir directamente).

Author: Alberto Pérez Bernabeu

Starting date: 21-11-2023
Last modification: 26-11-2023
"""
from random import randrange

ROWS = 4
COLUMNS = 10
MAX_HEIGHT = 210
MIN_HEIGHT = 140

matrix = []
paises = ["España", "Rusia", "Japón", "Australia"]

for r in range(ROWS):
    row = [randrange(MIN_HEIGHT, MAX_HEIGHT + 1) for c in range(COLUMNS)]
    matrix.append(row)

print("\n")
for r in range(ROWS):
    print(f"{paises[r]:<10s} ||", end="")
    for c in range(COLUMNS):
        print(f"{matrix[r][c]:^5d}", end="|")
        if c == (COLUMNS - 1):
            print("\n")

print("-------------------------------------------------------------------------")

for i in range(ROWS):
    print(f"En {paises[i]}, la altura mínima es de {min(matrix[i])} cm, la máxima es de {max(matrix[i])} cm y la "
          f"media es de {round(sum(matrix[i]) / COLUMNS)} cm.")

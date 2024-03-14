"""
Define tres arrays de 20 números enteros cada uno, con nombres número, cuadrado y cubo. Carga el array número con
valores aleatorios entre 0 y 100. En el array cuadrado se deben almacenar los cuadrados de los valores que hay en el
array número. En el array cubo se deben almacenar los cubos de los valores que hay en número. A continuación, muestra el
contenido de los tres arrays dispuesto en tres columnas.

Author: Alberto Pérez Bernabeu

Starting date: 19-11-2023
Last modification: 19-11-2023
"""
import random

LONGITUDE = 20
MIN = 1
MAX = 101

numero = []
for _ in range(0, LONGITUDE):
    numero += [random.randrange(MIN, MAX)]

cuadrado = []
for _ in numero:
    cuadrado += [_ ** 2]

cubo = []
for _ in numero:
    cubo += [_ ** 3]

print("\nNÚMERO | CUADRADO | CUBO\n----------------------------")

order = 0
for _ in range(LONGITUDE):
    print(f"{numero[order]:^6} | {cuadrado[order]:^8} | {cubo[order]:^7}\n----------------------------")
    order += 1

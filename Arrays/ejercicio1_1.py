"""
Escribe sentencias Python para realizar cada una de las siguientes tareas:

a) Muestra el valor del elemento 6 de un array f.
b) Inicializa los 5 primeros elementos de un array unidimensional de enteros a 8.
c) Total de los 100 elementos de punto-flotante de un array c.
d) Copia los 11 elementos de un array a en la primera porción de un array b, el cual contiene 34 elementos.
e) Calcula y muestra el valor mayor y menor contenidos en un array w de 99 elementos de punto-flotante

Author: Alberto Pérez Bernabeu

Starting date: 13-11-23
Last modification: 13-11-23
"""

# a)
f = [n for n in range(1, 8)]
print(f"El elemento 6 de una lista que almacena los números del 1 al 7 ({f}) es: {f[6]}.\n")


# b)
list1 = [8] * 5
print(f"Una lista cuyos cinco primeros elementos han sido inicializados a 8 es: {list1}.\n")

# c)
c = [0.0] * 100
print(f"{c[0:20]} \n{c[20:40]} \n{c[40:60]} \n{c[60:80]} \n{c[80:100]}")

# d)
b = [n for n in range(1, 35)]
list2 = b[0:11].copy()
print(f"\n{list2}")

# e)


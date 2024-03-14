"""
The program asks for a lower limit and an upper limit. Then, the user writes as many numbers he wants, but if 0 is
introduced, the program stops letting additional numbers being written. The program shows the sum of the numbers in
the interval, how many numbers are out of the interval and if any of the numbers introduced is equal to any of the
limits.

Author: Alberto Pérez Bernabeu

Starting date: 28-10-23
Last modification:
"""

from sys import exit

print("Este programa mostrará la suma de los números dentro de un intervalo que usted defina y la cantidad de "
      "números introducidos fuera de ese intervalo. Introduzca el número 0 para finalizar el programa.\n")

print("Introduzca los límites.\n")
while True:
    print("Por favor, asegúrese de que el límite inferior es menor que el límite superior.")
    lower_limit = int(input("Introduzca el límite inferior.\n"))
    upper_limit = int(input("Introduzca el límite superior.\n"))
    if lower_limit < upper_limit:
        break

outer_counter = 0
total_sum = 0
limit_counter = 0

while True:
    num = int(input("Introduzca un número:\n"))
    if num == 0:
        break
    elif num < lower_limit or num > upper_limit:
        outer_counter += 1
    elif num == lower_limit or num == upper_limit:
        limit_counter += 1
    elif lower_limit < num < upper_limit:
        total_sum += num

print(f"La suma de los números introducidos que se encuentran en el intervalo, asciende a {total_sum}.\n")
print(f"La cantidad de números introducidos que no se encuentran dentro del intervalo, asciende a {outer_counter}.")
if limit_counter != 0:
    print(f"Se ha introducido al menos un número equivalente a {lower_limit} ó a {upper_limit}.\n")
else:
    print(f"No se ha introducido ningún número equivalente a {lower_limit} ni a {upper_limit}.")
exit()

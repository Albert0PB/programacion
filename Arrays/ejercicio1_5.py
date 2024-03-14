"""
Realiza un programa que pida la temperatura media que ha hecho en cada mes de un determinado año y que muestre a
continuación un diagrama de barras horizontales con esos datos. Las barras del diagrama se pueden dibujar a base de
asteriscos o cualquier otro carácter.

Author: Alberto Pérez Bernabeu

Starting date: 19-11-2023
Last modification:
"""
from random import randrange

MONTHS = ["ENERO", "FEBRERO", "MARZO", "ABRIL", "MAYO", "JUNIO", "JULIO", "AGOSTO", "SEPTIEMBRE", "OCTUBRE",
          "NOVIEMBRE", "DICIEMBRE"]

temperature = []

"""
for _ in range(len(MONTHS)):
    temperature.append(randrange(0, 46))
"""

for _ in range(len(MONTHS)):
    while True:
        try:
            temperature.append(float(input(f"Introduzca la temperatura del mes de {MONTHS[_]}.\n")))
            break
        except ValueError:
            print("Asegúrese de introducir un valor numérico (puede ser decimal) que represente la temperatura media"
                  f"del mes de {MONTHS[_]}.\n")


print("          ", "    ", "    5    10   15   20   25   30   35   40   45")
print("          ", "   0", "------------------------------------------------- 50")

for _ in range(len(temperature)):
    print(f"{MONTHS[_]:<10s}", "    ", f"{round(temperature[_]) * '*'}")

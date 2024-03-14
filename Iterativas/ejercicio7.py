"""
A person acquires a product that has to be paid in 20 monthly periods with doubling amounts, starting with payments of
10 €, 20 € and 40 € in the first, second and third periods, respectively. This program shows the amount to pay in each
period and the total sum of money paid.

Author: Alberto Pérez Bernabeu

Starting date: 28-10-23
Last modification: 01-11-23
"""

print("Este programa muestra los pagos a realizar por la compra de un determinado producto.")

payment = 10
month = 0
total = 0
period = 1

while month != 20:
    print(f"El pago en el periodo {period} asciende a {payment} €.")
    month += 1
    payment *= 2
    total += payment
    period += 1
print(f"El pago total acumulado durante los 20 meses asciende a {total} €.")

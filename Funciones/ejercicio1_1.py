"""
Calculator.

Author: Alberto Pérez Bernabeu

Starting date: 03-12-2023
Last modification:
"""
from sys import exit

while True:
    try:
        num_a = int(input("Introduzca un número: "))
        break
    except ValueError:
        print("Asegúrese de introducir un valor numérico: ")

while True:
    try:
        num_b = int(input("Introduzca un número: "))
        break
    except ValueError:
        print("Asegúrese de introducir un valor numérico: ")

while True:
    print("\n----------------------")
    print("Sumar               1 ")
    print("Restar              2 ")
    print("Multiplicar         3 ")
    print("Dividir             4 ")
    print("Terminar            0 ")
    print("----------------------\n")

    while True:
        try:
            option = int(input("Introduzca el código de opción del cálculo que desea realizar: "))
            if option < 0 or option > 4:
                print("Asegúrese de introducir un código válido.")
            else:
                break
        except ValueError:
            print("Asegúrese de introducir un código numérico válido.")

    if option == 0:
        print("\nGracias por utilizar este programa.")
        exit()

    elif option == 1:
        print(f"{num_a} + {num_b} = {num_a + num_b}")

    elif option == 2:
        print(f"{num_a} - {num_b} = {num_a - num_b}")

    elif option == 3:
        print(f"{num_a} x {num_b} = {num_a * num_b}")

    elif option == 4:
        print(f"{num_a} : {num_b} = {num_a // num_b}")

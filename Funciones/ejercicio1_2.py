"""
Improved calculator.

Author: Alberto Pérez Bernabeu

Starting date: 03-12-2023
Last modification: 03-12-2023
"""
from sys import exit

while True:
    print("\n-------------------------")
    print("Introducir números     1 ")
    print("Sumar                  2 ")
    print("Restar                 3 ")
    print("Multiplicar            4 ")
    print("Dividir                5 ")
    print("Terminar               0 ")
    print("-------------------------\n")

    while True:
        try:
            option = int(input("Introduzca el código de opción del cálculo que desea realizar: "))
            if option < 0 or option > 5:
                print("Asegúrese de introducir un código válido.")
            else:
                break
        except ValueError:
            print("Asegúrese de introducir un código numérico válido.")

    num_a = 0
    num_b = 0
    if option == 0:
        print("\nGracias por utilizar este programa.")
        exit()

    elif option == 1:
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

    elif option == 2:
        print(f"{num_a} + {num_b} = {num_a + num_b}")

    elif option == 3:
        print(f"{num_a} - {num_b} = {num_a - num_b}")

    elif option == 4:
        print(f"{num_a} x {num_b} = {num_a * num_b}")

    elif option == 5:
        try:
            print(f"{num_a} : {num_b} = {num_a // num_b}")
        except ZeroDivisionError:
            print("No es posible dividir entre 0.")

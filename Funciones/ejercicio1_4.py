"""
Definitive calculator.

'Haz un programa que pida dos valores (a y b) y a continuación muestre un menú con cinco opciones: sumar, restar,
multiplicar, dividir y terminar. Cada opción llama a una función a la que se le pasan las dos variables y muestra el
resultado de la operación. Si se introduce una opción incorrecta se muestra un mensaje de error. El menú se volverá a
mostrar, a menos que no se dé a la opción terminar.

Modifica el programa anterior para que la introducción de las variables sea una opción del menú (la primera). Las
variables se inicializan a cero.

Modifica el programa anterior para que si no se introducen las dos variables desde la opción correspondiente no se
puedan ejecutar el resto de las opciones.

Crea una función para gestionar menús: recibe una lista de opciones, las muestra numeradas, pide una opción (por su
número) y devuelve la opción escogida. Modifica el último programa para que use esta función.'

Author: Alberto Pérez Bernabeu

Starting date: 03-12-2023
Last modification: 03-12-2023
"""

from sys import exit

OPTIONS = ["Terminar", "Introducir números", "Sumar", "Restar", "Multiplicar", "Dividir"]


def menu_display(menu_options, separation_length=10, decoration="-", decoration_length=33):
    print("\n", decoration * decoration_length)
    for i in range(len(menu_options)):
        print(f"{menu_options[i]:<60s}", " " * separation_length, f"{decoration} {i} {decoration}", sep="")
    print(decoration * (decoration_length + 1), "\n")
    return


def main():
    while True:
        menu_display(OPTIONS, 8, "~", 36)

        while True:
            try:
                option = int(input("Introduzca el código de opción del cálculo que desea realizar: "))
                if option < 0 or option > 5:
                    print("Asegúrese de introducir un código válido.")
                else:
                    break
            except ValueError:
                print("Asegúrese de introducir un código numérico válido.")

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
            try:
                print(f"{num_a} + {num_b} = {num_a + num_b}")
            except NameError:
                print("Asegúrese de seleccionar la opción 'Introducir números' antes de realizar ninguna operación.")

        elif option == 3:
            try:
                print(f"{num_a} - {num_b} = {num_a - num_b}")
            except NameError:
                print("Asegúrese de seleccionar la opción 'Introducir números' antes de realizar ninguna operación.")

        elif option == 4:
            try:
                print(f"{num_a} x {num_b} = {num_a * num_b}")
            except NameError:
                print("Asegúrese de seleccionar la opción 'Introducir números' antes de realizar ninguna operación.")

        elif option == 5:
            try:
                print(f"{num_a} : {num_b} = {num_a // num_b}")
            except ZeroDivisionError:
                print("No es posible dividir entre 0.")
            except NameError:
                print("Asegúrese de seleccionar la opción 'Introducir números' antes de realizar ninguna operación.")


if __name__ == "__main__":
    main()


"""
def menu(options_array) // menu(*options)
    if 0 <= option <= len(option)
    
array con longitudes de las opciones y max para escoger la que contenga más caracteres
"""
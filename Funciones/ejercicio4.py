"""
Haz un programa que muestre un menú y, usando las funciones anteriores, ejecute las siguientes opciones:

Muestra los números primos que hay entre 1 y 1000.
Muestra los números capicúa que hay entre 1 y 99999.
Muestra la moda de 50 números enteros aleatorios entre 1 y 10.
Muestra la mediana de 10 números enteros aleatorios entre 1 y 50.
Muestra el máximo y mínimo de 1000 números enteros aleatorios entre 1 y 50000.
Muestra la varianza de 10 números enteros aleatorios entre 1 y 5.

Author: Alberto Pérez Bernabeu

Starting date: 09-12-2023
Last modification:
"""


def main():
    import ejercicio2
    from util import statistics
    from sys import exit

    while True:
        OPTIONS = ["Muestra los números primos que hay entre 1 y 1000.",
                   "Muestra los números capicúa que hay entre 1 y 99999.",
                   "Muestra la moda de 50 números enteros aleatorios entre 1 y 10. (en obras)",
                   "Muestra la mediana de 10 números enteros aleatorios entre 1 y 50.",
                   "Muestra el máximo y mínimo de 1000 números enteros aleatorios entre 1 y 50000.",
                   "Muestra la varianza de 10 números enteros aleatorios entre 1 y 5.",
                   "Salir del programa."]

        ejercicio2.menu_display(OPTIONS)

        option = ejercicio2.code_verification(OPTIONS)

        match option:
            case 6:
                print("\nGracias por utilizar el programa.")
                exit()

            case 0:  # PRIMOS
                START = 1
                END = 1000
                order = 1
                for i in range(START, END + 1):
                    if ejercicio2.is_prime(i):
                        print(f"El primo número {order}º entre 1 y 1000 es {i}.")
                        order += 1

            case 1:  # CAPICÚAS
                START = 1
                END = 99999
                order = 1
                for i in range(START, END + 1):
                    if ejercicio2.is_palindrome(i):
                        print(f"El capicúa número {order}º entre 1 y 99999 es {i}.")
                        order += 1

            case 2:  # MODA
                START = 1
                END = 10
                numbers_array = ejercicio2.random_array_generation(START, END + 1, 50)


            case 3:  # MEDIANA
                START = 1
                END = 50
                numbers_array = ejercicio2.random_array_generation(START, END + 1, 10)
                print(f"La mediana del array es {statistics.median(numbers_array)}.")

            case 4:  # MAX y MIN
                numbers_array = ejercicio2.random_array_generation(1, 50000, 1000)
                print(f"El número mayor en el array es {statistics.maximum(numbers_array)}.\n"
                      f"El número menor en el array es {statistics.minimum(numbers_array)}.")

            case 5:  # VARIANZA
                numbers_array = ejercicio2.random_array_generation(1, 5, 10)
                print(f"La varianza en el array es {statistics.variance(numbers_array)}")


if __name__ == "__main__":
    main()

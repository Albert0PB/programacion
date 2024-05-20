"""
1. Modifica tu clase para gestionar menús de opciones en consola de forma que cuando el usuario introduzca 
una opción no entera se capture la excepción, se le advierta de que solo se admiten valores numéricos y se pida 
de nuevo la opción.
"""
from programacion.utils.menu import Menu


def main():
    while True:
        menu = Menu('Opción 1', 'Opción 2', 'Opción 3')

        menu.pick_option()


if __name__ == "__main__":
    main()

"""
2. Escribe un programa que sea capaz de leer el fichero anterior y lo muestre por la pantalla.

Author: Alberto Pérez Bernabeu
"""


def main():
    with open('primos.txt', 'r') as file:
        print(''.join(file.readlines()))


if __name__ == "__main__":
    main()

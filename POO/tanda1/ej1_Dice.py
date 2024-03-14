"""
Crea una clase "Dado" que simule el funcionamiento de un dado con caras del 1 al 6 que tienen la misma probabilidad de
salir y un programa de prueba.
"""
from random import randint


class Dice:
    def __init__(self):
        self.__faces = [1, 2, 3, 4, 5, 6]

    def roll(self):
        return self.__faces[randint(0, len(self.__faces) - 1)]


def main():
    die = Dice()
    print(die.roll())

    
if __name__ == "__main__":
    main()

"""
Implementar otra clase Dado. Por defecto el dado tendrá 6 caras. Tendremos tres formar de construir un dado (uno al que
no se le pasa nada e inicializa el dado al azar, otro al que sólo se le pasa que número tiene el dado en la cara
superior y otro con el número del dado en la cara superior y el número de caras del dado). Implementa los getters, el
método roll() que tirará el dado al azar y el __str__(). Implementa un tester que tenga un vector de 4 dados y los lance
una serie de veces.
"""
from random import randint
from typeguard import typechecked


@typechecked
class Dice:
    def __init__(self, faces_num: int = 6, front_face: int = 0):
        if faces_num < 1:
            raise ValueError('Número de caras del dado inválidas.')
        if front_face > faces_num:
            self.__faces_num = front_face
            self.__front_face = front_face
        elif front_face == 0:
            self.__faces_num = faces_num
            self.__front_face = randint(1, self.__faces_num)
        else:
            self.__faces_num = faces_num
            self.__front_face = front_face

    @property
    def faces_num(self):
        return self.__faces_num

    @property
    def front_face(self):
        return self.__front_face

    def roll(self):
        self.__front_face = randint(1, self.__faces_num)
        return self.__front_face

    def __str__(self):
        return f"Cara: {self.__front_face}, nº de caras: {self.__faces_num}"


def main():
    die1 = Dice()
    die2 = Dice()
    die3 = Dice()
    die4 = Dice()

    print(die1.roll())
    print(die2.roll())
    print(die3.roll())
    print(die4.roll())
    print(die1.roll())
    print(die2.roll())
    print(die3.roll())
    print(die4.roll())


if __name__ == "__main__":
    main()

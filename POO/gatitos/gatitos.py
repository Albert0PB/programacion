"""
Kittens that meow and sing!

Author: Alberto Pérez Bernabeu

El sonido de maullido es propiedad del usuario de freesound.org 'timtube'.
Licencia CC BY-NC 4.0 DEED (Atribución-NoComercial).
https://freesound.org/people/timtube/packs/3897/

La música utilizada es un fragmento de la canción 'Dubidubidu' de la artista Christell, lanzada en 2003.
"""
from playsound import playsound
from time import sleep


class Kittens:
    """Kittens meowing !!!"""

    def __init__(self, name, meowing):
        self.name = name
        self.meowing = meowing

    def meow(self):
        print(f"Maúlla, {self.name}!")
        sleep(1)
        playsound(self.meowing)


class SingingKittens(Kittens):
    """Kittens that learnt to sing !!!"""

    def sing(self):
        print(f"Canta, {self.name}!")
        sleep(1.5)
        playsound('/Prog/Trim2/OOP/gatitos/sonidos/songshort.wav')


def main():

    kitten1 = Kittens("Ámbar",
                      'C:/Users/Alber/PyProj/Prog/Trim2/OOP/gatitos/sonidos/meow3.wav')
    kitten2 = (
        SingingKittens("Lezo",
                       'C:/Users/Alber/PyProj/Prog/Trim2/OOP/gatitos/sonidos/meow4.wav')
    )

    kitten1.meow()
    kitten2.sing()
    kitten2.meow()


if __name__ == "__main__":
    main()

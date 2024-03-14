"""
12. Implementa la clase Mobile como subclase de Terminal (la clase del ejercicio anterior que ya no hace falta
modificar). Cada móvil lleva asociada una tarifa que puede ser “rata”, “mono” o “bisonte” (debes controlar esto).
El coste por minuto es de 6, 12 y 30 céntimos respectivamente. Se tarifican los segundos exactos. La tarifa se puede
cambiar. Obviamente, cuando un móvil llama a otro, se le cobra al que llama, no al que recibe la llamada. A continuación
 se proporciona el contenido del programa principal que usa esta clase y el resultado que debe aparecer por pantalla.
 El total tarificado debe aparecer con dos decimales.

Salida:

N.º 678 11 22 33 - 0 s de conversación - tarificados 0,00 euros
N.º 644 74 44 69 - 0 s de conversación - tarificados 0,00 euros
N.º 678 11 22 33 - 520 s de conversación - tarificados 0,52 euros
N.º 644 74 44 69 - 870 s de conversación - tarificados 1,10 euros
N.º 622 32 89 09 - 750 s de conversación - tarificados 0,00 euros
"""
from __future__ import annotations
from ej11_Terminal import Terminal
from typeguard import typechecked


@typechecked
class Mobile(Terminal):
    __TARIFFS = {'rata': 0.06, 'mono': 0.12, 'bisonte': 0.30}

    def __init__(self, cellphone_number, tariff):
        if tariff not in Mobile.__TARIFFS.keys():
            raise ValueError('Tarifa no reconocida.')
        self.__tariff = tariff
        self.__debt = 0
        super().__init__(cellphone_number)

    @classmethod
    def TARIFFS(cls):
        return cls.__TARIFFS

    @property
    def tariff(self):
        return self.__tariff

    @tariff.setter
    def tariff(self, value):
        self.__tariff = value

    @property
    def debt(self):
        return self.__debt

    def call(self, other: Terminal, duration_in_seconds):
        duration_in_minutes = duration_in_seconds / 60
        self.__debt += duration_in_minutes * Mobile.TARIFFS()[self.__tariff]
        super().call(other, duration_in_seconds)

    def __str__(self):
        return f'{super().__str__()} Tarificados {self.__debt:.2f} €'


def main():
    m1 = Mobile("678112233", "rata")
    m2 = Mobile("644744469", "mono")
    m3 = Mobile("622328909", "bisonte")
    print(m1)
    print(m2)
    m1.call(m2, 320)
    m1.call(m3, 200)
    m2.call(m3, 550)
    print(m1)
    print(m2)
    print(m3)


if __name__ == "__main__":
    main()

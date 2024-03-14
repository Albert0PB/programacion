"""
11. Implementa la clase Terminal. Un terminal tiene asociado un número de teléfono.
Los terminales se pueden llamar unos a otros y el tiempo de conversación corre para ambos.
A continuación se proporciona el contenido del programa principal que usa esta clase y el resultado que debe aparecer
por pantalla. Los números de teléfono tienen que validarse como tales al crear el objeto
(solo dígitos, empiezan por 9, 6 o 7, su longitud es de nueve dígitos) y no puede haber dos terminales con
el mismo número.


Salida:

No 678 11 22 33 - 0 s de conversación
No 644 74 44 69 - 0 s de conversación
No 678 11 22 33 - 520 s de conversación
No 644 74 44 69 - 320 s de conversación
No 622 32 89 09 - 200 s de conversación
No 664 73 98 18 - 0 s de conversación
"""
from __future__ import annotations
from typeguard import typechecked


@typechecked
class Terminal:
    __PHONE_NUMBER_LEN = 9
    __PHONE_NUMBER_STARTS = (9, 6, 7)

    __already_existing_numbers = []

    def __init__(self, phone_number: str):
        if Terminal.validate_phone_number(phone_number) and phone_number not in Terminal.already_existing_numbers():
            self.__phone_number = phone_number
            Terminal.already_existing_numbers().append(self.__phone_number)
        else:
            raise ValueError('¡Error! Número de teléfono inválido.')

        self.__call_time_in_seconds = 0

    @classmethod
    def PHONE_NUMBER_STARTS(cls):
        return cls.__PHONE_NUMBER_STARTS

    @classmethod
    def PHONE_NUMBER_LEN(cls):
        return cls.__PHONE_NUMBER_LEN

    @classmethod
    def already_existing_numbers(cls):
        return cls.__already_existing_numbers

    @staticmethod
    def validate_phone_number(candidate):
        if int(candidate[0]) in Terminal.PHONE_NUMBER_STARTS() and len(candidate) == Terminal.PHONE_NUMBER_LEN():
            return True
        return False

    def call(self, other: Terminal, duration_in_seconds: int):
        #  Implementar excepción en caso de que sea un número se llame a sí mismo
        if duration_in_seconds < 0:
            raise ValueError('No pueden existir cantidades de tiempo negativas.')
        self.__call_time_in_seconds += duration_in_seconds
        other.__call_time_in_seconds += duration_in_seconds

    def __str__(self):
        return f'N.º: {self.__phone_number} - {self.__call_time_in_seconds}s de conversación.'


def main():
    t1 = Terminal("678112233")
    t2 = Terminal("644744469")
    t3 = Terminal("622328909")
    t4 = Terminal("664739818")

    print(t1)
    print(t2)
    t1.call(t2, 320)
    t1.call(t3, 200)
    print(t1)
    print(t2)
    print(t3)
    print(t4)


if __name__ == "__main__":
    main()

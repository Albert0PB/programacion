from typeguard import typechecked
from abc import ABC


@typechecked
class Operation(ABC):
    def __init__(self, int_amount: int, dec_amount: int, currency_code: str):
        self.__int_amount = int_amount
        self.__dec_amount = dec_amount
        self.__currency_code = currency_code

    @property
    def int_amount(self):
        return self.__int_amount

    @int_amount.setter
    def int_amount(self, value):
        if value < 0:
            raise ValueError("No puede realizarse una operación con valores monetarios negativos.")
        self.__int_amount = value

    @property
    def dec_amount(self):
        return self.__dec_amount

    @dec_amount.setter
    def dec_amount(self, value):
        if value >= 100:
            self.__int_amount += value // 100
            self.__dec_amount = value % 100
        else:
            self.__dec_amount = value

    @property
    def currency_code(self):
        return self.__currency_code

    @currency_code.setter
    def currency_code(self, value):
        if len(value) != 3:
            raise ValueError(f"La moneda se indica con un código de 3 letras. Introducido: '{value}'")
        self.__currency_code = value


"""
Crea una clase "Fraction" inmutable (no hay setters, solo getters para numerador y denominador) de forma que podamos
hacer las siguientes operaciones:

    - Construir un objeto Fracción pasándole al constructor el numerador y el denominador. La fracción se construye
      simplificada, no se puede dividir por cero.                                                                      *
    - Obtener resultado de la fracción (número real).                                                                  *
    - Multiplicar la fracción por un número (el método devuelve otra fracción, simplificada).                          *
    - Multiplicar, dividir, sumar y restar fracciones (los métodos devuelven otra fracción, simplificada).
    - Comparar fracciones entre sí o con enteros usando los operadores relacionales.
"""
from __future__ import annotations
from typeguard import typechecked
from math import gcd
from typing import Union


@typechecked
class Fraction:
    def __init__(self, numerator: int, denominator: int):
        if denominator == 0:
            raise ZeroDivisionError("Error. No se puede dividir entre 0.")

        common_divisor = gcd(numerator, denominator)

        self.__numerator = numerator // common_divisor
        self.__denominator = denominator // common_divisor

    @property
    def numerator(self):
        return self.__numerator

    @property
    def denominator(self):
        return self.__denominator

    @property
    def result(self):
        return self.__numerator / self.__denominator

    def __mul__(self, other: Union[int, Fraction]):
        if isinstance(other, int):
            return Fraction(self.__numerator * other, self.__denominator)
        else:
            return Fraction(self.__numerator * other.__numerator, self.__denominator * other.__denominator)

    def __rmul__(self, other: int):
        self * other

    def __truediv__(self, other: Fraction):
        return Fraction(self.__numerator * other.__denominator, self.__denominator * other.__numerator)

    def __add__(self, other: Fraction):
        return Fraction(self.__numerator * other.__denominator + other.__numerator * self.__denominator,
                        self.__denominator * other.__denominator)

    def __sub__(self, other: Fraction):
        return Fraction(self.__numerator * other.__denominator - other.__numerator * self.__denominator,
                        self.__denominator * other.__denominator)

    def __neg__(self):
        return self * -1

    def __str__(self):
        return f'{self.__numerator}/{self.__denominator}'


def main():
    pass


if __name__ == "__main__":
    main()

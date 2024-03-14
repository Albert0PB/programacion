"""
Crea una clase para almacenar duraciones de tiempo (Duration). Los objetos de esta clase son intervalos de tiempo y se
crean de la forma:

    - t1 = Duration(1, 20, 30)  # almacenará 1 hora, 20 minutos y 30 segundos.

    - t2 = Duration(2, 75, -10)  # almacenará 3 horas, 14 minutos y 50 segundos.

    - t3 = Duration(t2)  # almacenará las horas, minutos y segundos del objeto t2

Crea los getters y setters mediante propiedades y métodos para:

    - Sumar y restar objetos de la clase sobrecargando operadores (el resultado es otro objeto).
    - Sumar y restar segundos, minutos u horas (se cambia el objeto actual).
    - Devolver una cadena con el tiempo almacenado, de forma que si lo que hay es (10 35 5) la cadena sea 10 h 35 m 5 s.
"""
from __future__ import annotations
from typeguard import typechecked
from typing import Union
#  TODO: duration to seconds in independent function


@typechecked
class Duration:
    def __init__(self, hours: Union[int, Duration], minutes: Union[int, None] = None, seconds: Union[int, None] = None):
        if isinstance(hours, Duration) and minutes is None and seconds is None:
            other = hours
            self.__hours = other.hours
            self.__minutes = other.minutes
            self.__seconds = other.seconds
        elif isinstance(hours, int) and isinstance(minutes, int) and isinstance(seconds, int):
            self.__hours = hours
            self.__minutes = minutes
            self.__seconds = seconds
        else:
            raise TypeError("Los objetos de la clase Duration se construyen a partir de otro objeto Duration o de tres"
                            "enteros.")
        self.normalization()

    @property
    def hours(self):
        return self.__hours

    @property
    def minutes(self):
        return self.__minutes

    @property
    def seconds(self):
        return self.__seconds

    def __str__(self):
        return f'{self.__hours}h {self.__minutes}m {self.__seconds}s'

    def add_hours(self, hours_to_add: int):
        self.__hours += hours_to_add
        try:
            self.normalization()
        except ValueError:
            raise ValueError("¡Error! La duración calculada es negativa.")

    def add_minutes(self, minutes_to_add: int):
        self.__minutes += minutes_to_add
        try:
            self.normalization()
        except ValueError:
            raise ValueError("¡Error! La duración calculada es negativa.")

    def add_seconds(self, seconds_to_add: int):
        self.__seconds += seconds_to_add
        try:
            self.normalization()
        except ValueError:
            raise ValueError("¡Error! La duración calculada es negativa.")

    def __add__(self, other: Duration):
        result_hours = self.__hours + other.__hours
        result_minutes = self.__minutes + other.__minutes
        result_seconds = self.__seconds + other.__seconds
        Duration(result_hours, result_minutes, result_seconds).normalization()
        return Duration(result_hours, result_minutes, result_seconds)

    def __sub__(self, other: Duration):
        result_hours = self.__hours - other.__hours
        result_minutes = self.__minutes - other.__minutes
        result_seconds = self.__seconds - other.__seconds
        Duration(result_hours, result_minutes, result_seconds).normalization()
        return Duration(result_hours, result_minutes, result_seconds)

    def positive_check(self):
        duration_in_seconds = self.__hours * 3600 + self.__minutes * 60 + self.__seconds
        if duration_in_seconds < 0:
            raise ValueError("No puede introducirse una duración negativa")
        return duration_in_seconds

    def normalization(self):
        self.__hours = self.positive_check() // 3600
        self.__minutes = self.positive_check() % 3600 // 60
        self.__seconds = self.positive_check() - self.__hours * 3600 - self.__minutes * 60


def main():
    duration_tester = Duration(0, 0, 0)

    d = Duration(duration_tester)

    duration_tester.add_hours(1)
    print(duration_tester)
    duration_tester.add_hours(-1)
    print(duration_tester)

    duration_tester.add_minutes(1)
    print(duration_tester)
    duration_tester.add_minutes(-1)
    print(duration_tester)
    duration_tester.add_minutes(60)
    print(duration_tester)
    duration_tester.add_minutes(-60)
    print(duration_tester)

    duration_tester.add_seconds(1)
    print(duration_tester)
    duration_tester.add_seconds(60)
    print(duration_tester)
    duration_tester.add_seconds(3600)
    print(duration_tester)
    duration_tester.add_seconds(-3600)
    print(duration_tester)
    duration_tester.add_seconds(-60)
    print(duration_tester)
    duration_tester.add_seconds(-1)
    print(duration_tester)


if __name__ == "__main__":
    main()

"""
Crea la clase abstracta Vehicle, así como las clases Bike y Car como subclases de la primera. Para la clase Vehicle,
crea los atributos de clase vehicles_created y total_kilometers, así como el atributo de instancia kilometers_traveled.

En la clase Vehicle crea un método para viajar (travel) que incremente los kilómetros recorridos.

En la clase Bike haz un método para hacer el caballito.

En la clase Car:

    - Tendremos una variable de instancia con los litros de combustible que quedan en el depósito, inicialmente cero.

    - Tendremos un método para quemar rueda y otro para llenar el depósito.

    - Cuando el coche viaje disminuirá el número de litros en el depósito en relación con los kilómetros viajados. Si no
    hay combustible suficiente, el coche recorrerá únicamente los kilómetros que pueda.

    - Para simplificar, cada kilómetro recorrido consumirá 0,1 litros de combustible, en un depósito caben 50 litros y
    quemar rueda consume 1 litro de combustible.

    - Prueba las clases creadas mediante un programa con un menú (usando la clase de la tanda anterior) como el que se
    muestra a continuación:

VEHÍCULOS
=========
1. Anda con la bicicleta.
2. Haz el caballito con la bicicleta.
3. Anda con el coche.
4. Quema rueda con el coche.
5. Llena el depósito del coche.
6. Ver kilometraje de la bicicleta.
7. Ver kilometraje del coche.
8. Ver el combustible que queda en el depósito del coche.
9. Ver kilometraje total.
10. Salir.

Elige una opción (1-8):

Author: Alberto Pérez Bernabeu
"""
from __future__ import annotations
from typeguard import typechecked
from Prog.Trim2.OOP.tanda2.ej8.menu import Menu
from abc import ABC
from random import choice


def pos_float_input():
    while True:
        pos_float = float(input('Indique una cantidad positiva (puede ser decimal): '))
        if pos_float >= 0 and isinstance(pos_float, float):
            return pos_float
        print('Por favor, asegúrese de indicar una cantidad positiva.')


@typechecked
class Vehicle(ABC):
    __vehicles_created = 0
    __total_kilometers = 0.0

    def __init__(self):
        self.__kilometers_traveled = 0.0

    @property
    def kilometers_traveled(self):
        return self.__kilometers_traveled

    @classmethod
    def vehicles_created(cls):
        return cls.__vehicles_created

    @classmethod
    def total_kilometers(cls):
        return cls.__total_kilometers

    def travel(self):
        kilometers_to_travel = pos_float_input()
        Vehicle.__total_kilometers += kilometers_to_travel
        self.__kilometers_traveled += kilometers_to_travel
        if isinstance(self, Car):
            if kilometers_to_travel > self.fuel * 10:
                kilometers_to_travel = self.fuel * 10
                print(f'Sólo tienes gasolina para {kilometers_to_travel} kilómetros.')
            self.fuel -= kilometers_to_travel * 0.1

        print(f'Has recorrido {kilometers_to_travel} kilómetros.')


@typechecked
class Bike(Vehicle):
    def __init__(self):
        super().__init__()

    @staticmethod
    def do_a_wheelie():
        return f'Haces un caballito... {choice(('Y te la has pegado...', '¡Guay!'))}'


@typechecked
class Car(Vehicle):
    TANK_MAX_CAPACITY = 50.0

    def __init__(self):
        self.__fuel = 0.0
        super().__init__()

    @property
    def fuel(self):
        return self.__fuel

    @fuel.setter
    def fuel(self, value):
        if isinstance(value, float):
            self.__fuel = value

    def refill_tank(self):
        self.__fuel = Car.TANK_MAX_CAPACITY
        print('Rellenas el depósito al máximo.')

    def burnout(self):
        if self.__fuel < 1.0:
            return 'No te queda gasolina como para performar a tanto nivel...'
        self.__fuel -= 1.0
        return f'Quemas rueda... {choice(('Los vecinos se quejan del ruido...', '¡Vas a tope!'))}'


def main():
    b = Bike()
    c = Car()
    vehicles_menu = Menu('Salir', 'Anda con la bicicleta', 'Haz el caballito con la bicicleta',
                         'Anda con el coche', 'Quema rueda con el coche', 'Llena el depósito del coche',
                         'Ver kilometraje de la bicicleta', 'Ver kilometraje del coche',
                         'Ver el combustible que queda en el depósito del coche', 'Ver kilometraje total')

    while True:
        selected = vehicles_menu.pick_option()

        match selected:
            case 0:
                print('Gracias por utilizar este programa.')
                exit(0)
            case 1:
                b.travel()
            case 2:
                print(b.do_a_wheelie())
            case 3:
                c.travel()
            case 4:
                print(c.burnout())
            case 5:
                c.refill_tank()
            case 6:
                print(b.kilometers_traveled)
            case 7:
                print(c.kilometers_traveled)
            case 8:
                print(c.fuel)
            case 9:
                print(f'{Vehicle.total_kilometers()} kilómetros recorridos en total.')


if __name__ == "__main__":
    main()

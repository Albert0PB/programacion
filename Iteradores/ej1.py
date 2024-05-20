"""
Crea el iterador PrimeIterator que permita iterar sobre la lista de números primos, desde 2 hasta uno dado como máximo.
Ejemplo: "primes = list(PrimeIterator(15)) devolverá [2, 3, 5, 7, 11, 13]"

Author: Alberto Pérez Bernabeu
Starting date: 13/5/2024
Last modification: 14/5/2024
"""
from collections.abc import Iterator
from typeguard import typechecked


@typechecked
class PrimeIterator(Iterator):
    def __init__(self, limit: int):
        if limit < 2:
            raise ValueError(f"Los objetos de esta clase se construyen pasando como parámetro un entero mayor a dos. "
                             f"Introducido: {limit}")
        self.__limit = limit
        self.__candidate = 2

    def __next__(self):
        while self.__candidate <= self.__limit:
            if self.__true_if_prime(self.__candidate):
                next_ = self.__candidate
                self.__candidate += 1
                return next_
            self.__candidate += 1
        raise StopIteration

    def __iter__(self):
        return self

    @staticmethod   
    def __true_if_prime(n):
        num = 2
        while num <= round(n ** (1/2)):
            if n % num == 0:
                return False
            num += 1
        return True 


def main():
    primes = PrimeIterator(15)
    print(list(primes))


if __name__ == '__main__':
    main()

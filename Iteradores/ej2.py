"""
2- Haz el ejercicio anterior usando una lista interna y eliminando elementos con el algoritmo de la criba de
Eratóstenes.

Author: Alberto Pérez Bernabeu
Starting date: 15/5/2024
Last modification: 18/5/2024
"""
from collections.abc import Iterator
from typeguard import typechecked


@typechecked
class PrimeIterator(Iterator):
    def __init__(self, limit):
        if limit <= 2:
            raise ValueError("Los objetos de esta clase se construyen pasándoles un entero mayor que 2 como parámetro.")
        self.__list = [i for i in range(2, limit+1)]
        self.__eratosthenes()
        self.__index = -1

    def __eratosthenes(self):
        primes = list()
        for i in self.__list:
            if self.__true_if_prime(i):
                primes.append(i)
        for prime in primes:
            for j in self.__list:
                if j % prime == 0:
                    self.__list.remove(j)
        self.__list = sorted((self.__list + primes))

    @staticmethod
    def __true_if_prime(n):
        num = 2
        while num <= round(n ** (1 / 2)):
            if n % num == 0:
                return False
            num += 1
        return True

    def __next__(self):
        self.__index += 1
        return self.__list[self.__index]

    def __iter__(self):
        return self.__list.__iter__()


def main():
    print(list(PrimeIterator(34)))


if __name__ == "__main__":
    main()

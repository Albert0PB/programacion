"""
4. Vamos a crear una lista de 100 números enteros aleatorios entre -5000 y 5000 y vamos a averiguar:

        Usando map:
            Una lista con los números elevados al cuadrado.
            Una lista con los números como cadena de texto.
        Usando filter:
            Los números múltiplos de 3.
            El total de números negativos.
            Los números primos.
            El máximo número primo.
        Usando reduce:
            La suma de todos los números.
            La suma de todos los números pares.T
            La multiplicación de todos los números primos.

Author: Alberto Pérez Bernabeu
Starting date: 15/5/2024
Last modification: 21/5/2024
"""
import random
import inflect
import math
from functools import reduce

LOWER_LIMIT = -5000
UPPER_LIMIT = 5000
NUMBERS_TO_GENERATE = 100


def true_if_prime(n):
    if n < 2:
        return False
    num = 2
    while num <= round(math.sqrt(n)):
        if n % num == 0:
            return False
        num += 1
    return True


def true_if_pair(n):
    return True if n % 2 == 0 else False


random_list = list((random.randint(LOWER_LIMIT, UPPER_LIMIT) for i in range(NUMBERS_TO_GENERATE)))
num_namer = inflect.engine()

# Uso de map
squares = list(map(lambda x: x ** 2, random_list))
strings = list(map(lambda x: num_namer.number_to_words(x), random_list))

# Uso de filter
multiples_of_three = filter(lambda x: True if x % 3 == 0 else False, random_list)
negatives = filter(lambda x: True if x < 0 else False, random_list)
primes = filter(lambda x: true_if_prime(x), random_list)

# Uso de reduce
total_sum = reduce(lambda total, x: total + x, random_list)
evens_sum = reduce(lambda total, x: total + x, set(filter(lambda x: True if x % 2 == 0 else False, random_list)))
primes_product = reduce(lambda total, x: total + x, primes)

if __name__ == "__main__":
    print('Lista base generada aleatoriamente:\n', random_list, '\n')

    # Usando map
    print('Lista de cuadrados:\n', squares, '\n')
    print('Lista de cadenas:\n', strings, '\n')

    # Usando filter
    print('Múltiplos de tres filtrados de la lista:\n', multiples_of_three, '\n')
    print('Total de números negativos:\n', negatives, '\n')
    print('Números primos:\n', primes, '\n')
    print('Máximo primo generado:', max(primes), '\n')

    # Uso de reduce
    print('Suma total:', total_sum, '\n')
    print('Suma de pares:', evens_sum, '\n')
    print('Producto de primos:', primes_product, '\n')

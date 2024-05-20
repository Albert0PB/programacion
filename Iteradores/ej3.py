"""
3. Haz el ejercicio 1 usando una función generadora.

Author: Alberto Pérez Bernabeu
Starting date: 15/5/2024
Last modification:
"""
import math


def true_if_prime(n):
    if n < 2:
        return False
    num = 2
    while num <= round(math.sqrt(n)):
        if n % num == 0:
            return False
        num += 1
    return True


def prime_generator(limit):
    prime_candidate = 2
    while prime_candidate <= limit:
        if true_if_prime(prime_candidate):
            yield prime_candidate
        prime_candidate += 1


def main():
    primes = []
    for i in prime_generator(23):
        primes.append(i)
    print(primes)


if __name__ == "__main__":
    main()

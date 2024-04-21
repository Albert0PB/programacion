"""
1. Escribe un programa que guarde en un fichero con nombre primos.txt los números primos que hay entre 1 y 500.

Author: Alberto Pérez Bernabeu
"""


def true_if_prime(n):
    num = 2
    while num <= round(n ** (1/2)):
        if n % num == 0:
            return False
        num += 1
    return True


def generate_primes(start, stop):
    primes = []
    for n in range(start, stop + 1):
        if true_if_prime(n):
            primes.append(str(n))
    return "\n".join(primes)


def main():
    with open('primos.txt', mode='w') as file:
        file.write(generate_primes(1, 500))


if __name__ == "__main__":
    main()

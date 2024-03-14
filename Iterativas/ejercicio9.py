"""
Program that shows the first N prime numbers.

Author: Alberto Pérez Bernabeu

Starting date: 06-11-23
Last modification:
"""

print("Este programa le mostrará la cantidad de números primos que desee.\n")


prime_quantity = int(input("Introduzca la cantidad de números primos que desea obtener.\n"))


# Para comprobar que un número sea primo hay que confirmar que no tiene divisores entre el 3 y
# la raíz cuadrada del candidato a primo.

prime_candidate = 3
prime_order = 1
denominator = 1
is_prime = True

print(f"{prime_order}: 2")
prime_order += 1

while prime_quantity != 1:
    while is_prime:
        for n in range(1, round(prime_candidate ** (1/2))):
            if prime_candidate // n != 0:
                print(f"{prime_order}: {prime_candidate}")
                prime_order += 1
                prime_quantity -= 1
            else:
                is_prime = False
            prime_candidate += 2

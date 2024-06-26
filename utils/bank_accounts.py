from __future__ import annotations
from typeguard import typechecked
from random import randint


def account_number_generator():
    return (f'{randint(0, 9)}{randint(0, 9)}{randint(0, 9)}{randint(0, 9)}'
            f'{randint(0, 9)}{randint(0, 9)}{randint(0, 9)}{randint(0, 9)}'
            f'{randint(0, 9)}{randint(0, 9)}')


@typechecked
def check_positive_quantity(quantity: (int, float)):
    if quantity < 0:
        raise ValueError('No se permiten cantidades monetarias negativas.')
    return


@typechecked
class BankAccount:
    # Implementar Initial Balance para la creación de cuentas con saldos iniciales positivos

    __existent_accounts = []

    def __init__(self, credit: float = 0.0):
        while True:
            account_number_candidate = account_number_generator()
            if account_number_candidate not in BankAccount.__existent_accounts:
                BankAccount.__existent_accounts.append(account_number_candidate)
                self.__account_number = account_number_candidate
                break
        self.__credit = credit
        self.__account_historic = {}

    def deposit(self, quantity: float):
        check_positive_quantity(quantity)
        self.__credit += quantity
        self.__account_historic.update({f'Ingreso de {quantity:.2f} €.': self.__credit})

    def withdraw(self, quantity: float):
        check_positive_quantity(quantity)
        self.__credit -= quantity
        self.__account_historic.update({f'Cargo de {quantity:.2f} €.': self.__credit})

    def transfer(self, other: BankAccount, quantity: float):
        check_positive_quantity(quantity)
        self.__credit -= quantity
        self.__account_historic.update({f'Transferencia emitida de {quantity:.2f} € a la cuenta '
                                        f'{other.__account_number}': self.__credit})
        other.__credit += quantity
        other.__account_historic.update({f'Transferencia recibida de {quantity:.2f} € de la cuenta '
                                         f'{self.__account_number}': other.__credit})

    def show_account_historic(self):
        historic_str = ''
        for index, movement in enumerate(self.__account_historic.keys()):
            historic_str += (f'{list(self.__account_historic.keys())[index]} - '
                             f'Saldo {self.__account_historic[movement]:.2f} €\n')
        return historic_str

    def __str__(self):
        return f'N.º de cta.: {self.__account_number} Saldo: {self.__credit:<8.2f} €'


def main():
    cuenta1 = BankAccount()
    cuenta2 = BankAccount(1500)
    cuenta3 = BankAccount(6000)
    print(cuenta1)
    print(cuenta2)
    print(cuenta3)
    cuenta1.deposit(2000)
    cuenta2.withdraw(600)
    cuenta3.deposit(75)
    cuenta1.withdraw(55)
    cuenta2.transfer(cuenta3, 100)
    print(cuenta1)
    print(cuenta2)
    print(cuenta3)
    """
    Salida

Número de cta.: 6942541557 Saldo: 0,00 €
Número de cta.: 9319536518 Saldo: 1500,00 €
Número de cta.: 7396941518 Saldo: 6000,00 €
Número de cta.: 6942541557 Saldo: 1945,00 €
Número de cta.: 9319536518 Saldo: 800,00 €
Número de cta.: 7396941518 Saldo: 6175,00 €
"""


if __name__ == "__main__":
    main()

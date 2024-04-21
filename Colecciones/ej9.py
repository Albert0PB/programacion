"""
9. Amplía el ejercicio de la tanda anterior que implementaba cuentas corrientes de un banco de tal forma que cada
cuenta lleve un registro de todos los movimientos realizados: ingresos, cargos y transferencias (tanto enviadas
como recibidas).

Salida:

Movimientos de la cuenta 1654432813
-----------------------------------
Ingreso de 2000 € Saldo: 2000,00 €
Cargo de 600 € Saldo: 1400,00 €
Cargo de 55 € Saldo: 1345,00 €
Transferencia recibida de 100 € de la cuenta 1654432813 Saldo 1445,00 €
Transferencia emitida de 250 € a la cuenta 6546817008 Saldo 1195,00 €
Transferencia recibida de 22 € de la cuenta 1654432813 Saldo 1217,00 €
"""
from repo.utils.bank_accounts import BankAccount


def main():
    cuenta1 = BankAccount()
    cuenta2 = BankAccount(1500)
    cuenta3 = BankAccount(6000)
    cuenta1.deposit(2000)
    cuenta1.withdraw(600)
    cuenta3.deposit(75)
    cuenta1.withdraw(55)
    cuenta2.transfer(cuenta1, 100)
    cuenta1.transfer(cuenta3, 250)
    cuenta3.transfer(cuenta1, 22)
    print(cuenta1.show_account_historic())


if __name__ == "__main__":
    main()

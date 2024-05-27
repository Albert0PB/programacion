"""
1. Modifica el ejercicio de la cuenta corriente para que el método que almacena en un fichero el estado del objeto
guarde el objeto entero y el que lo recupera lo restaure. En esta versión no le pasamos nombre de fichero al método a
la hora de guardarlo, usará el número de cuenta corriente para ello.

Author: Alberto Pérez Bernabeu
"""
from utils.bank_accounts import BankAccount
import os
import pickle


class PickleBankAccount(BankAccount):
    def __init__(self):
        super().__init__()

    def save_as_pickle(self):
        with open(f"{self.__account_number}.pkl", 'wb') as file:
            pickle.dump(self, file)

    @staticmethod
    def load_from_pickle(pickle_file):
        account, file_ext = os.path.splitext(pickle_file)
        if file_ext != '.pkl':
            raise ValueError("El fichero seleccionado no posee extensión '.pkl'.")
        return pickle.loads(pickle_file)

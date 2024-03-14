"""
1. Implementa el control de acceso al área restringida de un programa. Se debe pedir un nombre de usuario y una
contraseña. Si el usuario introduce los datos correctamente, el programa dirá “Ha accedido al área restringida”.

El usuario tendrá un máximo de 3 oportunidades. Si se agotan las oportunidades el programa dirá “Lo siento, no tiene
acceso al área restringida”. Los nombres de usuario con sus correspondientes contraseñas deben estar almacenados en un
diccionario.

Author: Alberto Pérez Bernabeu
"""
from Prog.Trim2.OOP.tanda2.ej8.menu import Menu
from sys import exit
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

users = {}


def input_user_name():
    return str(input('Indique su nombre de usuario: '))


def input_user_password():
    return str(input('Indique su contraseña: '))


def login():
    account_attempted_login = input_user_name()
    if account_attempted_login in users and input_user_password() == users[account_attempted_login]:
        print('Ha accedido al área restringida.')
        return True
    return False


def register():
    while True:
        name = input_user_name()
        if name not in users.keys():
            users.update({name: input_user_password()})
            break
        print('Ese nombre de usuario ya existe. Por favor, escoja un nombre diferente.')


def chamber_of_secrets():
    treasure_path = 'treasure.jpg'
    treasure = mpimg.imread(treasure_path)
    treasure_show = plt.imshow(treasure)
    plt.show()


def main():
    menu = Menu('Salir', 'Registrarse', 'Iniciar sesión')

    while True:
        select = menu.pick_option()
        match select:
            case 0:
                exit('Gracias por utilizar este programa.')

            case 1:
                print('Indique sus datos de registro.')
                register()

            case 2:
                attempts = 0
                for i in range(3):
                    print('Indique sus datos de inicio de sesión.')
                    if login():
                        chamber_of_secrets()
                        break
                    attempts += 1
                if attempts == 3:
                    exit('Lo siento. No tiene acceso al área restringida.')


if __name__ == "__main__":
    main()

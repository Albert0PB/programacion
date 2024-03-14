from typeguard import typechecked


@typechecked
class Menu:
    def __init__(self, *options: str):
        self.__options = list(options)

    @property
    def options(self):
        return self.__options

    def __str__(self):
        menu_str = '\n'
        for i in range(len(self.__options)):
            menu_str += f'{i + 1}- {self.__options[i]}\n'
        menu_str += '\n'
        return menu_str

    def pick_option(self):
        print(self)
        try:
            chosen_one = int(input('Indique la opción que desea escoger (debe ser un número entero): '))
        except TypeError or ValueError:
            print("Asegúrese de introducir un número entero para indicar la opción que desea seleccionar.")

        if 0 < chosen_one <= len(self.__options):
            return chosen_one - 1
        print('La opción seleccionada no existe.')

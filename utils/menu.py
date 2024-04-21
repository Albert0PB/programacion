from typeguard import typechecked


class OptNotPosInt(Exception):
    def __init__(self, value):
        super().__init__(f"La opción seleccionada debe ser un número entero. Introducido: '{value}'.")
        self.value = value


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
        chosen_one = input('Indique la opción que desea escoger (debe ser un número entero): ')

        try:
            chosen_one = int(chosen_one)
            if chosen_one < 0:
                raise OptNotPosInt(chosen_one)
        except ValueError:
            raise OptNotPosInt(chosen_one)
        except OptNotPosInt as e:
            print(f'La opción introducida debe ser un entero positivo. Recibido: "{e.value}"')

        if 0 < chosen_one <= len(self.__options):
            return chosen_one - 1

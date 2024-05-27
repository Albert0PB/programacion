"""
2. Crea un programa que encripte un fichero que le pasamos como parámetro y almacene el resultado en otro, que también
pasamos como parámetro, de manera que:

Si el programa no recibe el número de parámetros adecuado termina con un error 1.

Si el programa recibe un solo parámetro guardará la información encriptada en el mismo archivo del que lee, pero antes
advertirá al usuario de que machacará el archivo origen, dando opción a que la operación no se haga.

Si el fichero origen no existe (da error al abrirlo como lectura) el programa termina con un mensaje de error y
código 2.

Si en el fichero destino no se puede escribir (da error al abrirlo como escritura) el programa termina con un mensaje
de error y código 3.

Para encriptar usa el método César, necesitarás una clave que debes pedir al usuario.

Author: Alberto Pérez Bernabeu
"""
import sys

BASE_CORRESPONDENCES = {0: 'A', 1: 'B', 2: 'C', 3: 'D', 4: 'E', 5: 'F', 6: 'G', 7: 'H', 8: 'I', 9: 'J', 10: 'K', 
                        11: 'L', 12: 'M', 13: 'N', 14: 'Ñ', 15: 'O', 16: 'P', 17: 'Q', 18: 'R', 19: 'S', 20: 'T',
                        21: 'U', 22: 'V', 23: 'W', 24: 'X', 25: 'Y', 26: 'Z'}

LETTERS = "A B C D E F G H I J K L M N Ñ O P Q R S T U V W X Y Z".split()


def check_argv():
    if len(sys.argv) < 2:
        print("Código de Error 1: no se ha pasado ningún argumento a este programa.", file=sys.stderr)
    elif len(sys.argv) == 2:
        while True:
            keep_going = input("Sólo ha indicado un fichero, por lo que el texto encriptado se sobreescribirá en él. "
                               "¿Desea continuar? [S/N]\n")
            if keep_going.upper() == "S":
                print("El programa continuará ejecutándose.")
                break
            elif keep_going.upper() == "N":
                exit("Programa finalizado.")
            else:
                print(f"Por favor, indique 'S' o 'N'. Ha introducido: {keep_going}")
    elif len(sys.argv) > 3:
        exit("Ha indicado demasiados argumentos. Este programa funciona pasándole un fichero de texto a encriptar y, "
             "opcionalmente, un fichero de destino sobre el que escribir el texto encriptado.")


def input_int(msg: str = ""):
    while True:
        try:
            integer = int(input(msg))
            return integer
        except ValueError:
            print(f"Asegúrese de introducir un número entero. Ha introducido: '{integer}'.")


def main():
    check_argv()

    caesar_addend = input_int("Indique, con un entero, el número de posiciones que debe 'desplazarse' cada letra "
                              "del texto a encriptar (método César): ")

    try:
        encrypted_text = ""
        with open(sys.argv[1], "r") as file:
            for line in file.read():
                for char in line:
                    if char.isalpha():
                        char_to_add = LETTERS.index(char.upper()) + caesar_addend
                        char_to_add -= 26 if char_to_add > 26 else 0
                        encrypted_text += BASE_CORRESPONDENCES[char_to_add]
                    else:
                        encrypted_text += char

        try:
            if len(sys.argv) == 2:
                with open(sys.argv[1], "w") as file:
                    file.write(encrypted_text)
            else:
                with open(sys.argv[2], "w") as file:
                    file.write(encrypted_text)
        except (FileNotFoundError, PermissionError) as e:
            print(f"Código de Error 3: {e}", file=sys.stderr)

    except (FileNotFoundError, PermissionError) as e:
        print(f"Código de Error 2: {e}", file=sys.stderr)
    finally:
        print("Programa finalizado.")


if __name__ == "__main__":
    main()

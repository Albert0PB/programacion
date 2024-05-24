"""
3. Realiza un programa que diga cuántas ocurrencias de una palabra hay en un fichero. Tanto el nombre del fichero como
la palabra se deben pasar como argumentos en la línea de comandos.

Author: Alberto Pérez Bernabeu
"""
import sys


def main():
    if len(sys.argv) != 3 or not all(isinstance(argv, str)for argv in sys.argv[1:]):
        raise ValueError("A este programa se le deben pasar dos argumentos: el nombre un fichero de texto existente y "
                         "una palabra.",
                         f"Argumentos pasados: {sys.argv[1:]}")

    try:
        with open(sys.argv[1], 'r') as file:
            word_to_count = sys.argv[2]
            words = file.read().split()
            reps = 0

            for word in words:
                reps += 1 if word == word_to_count else 0

            print(f"'{word_to_count}' se repite {reps} veces en el fichero '{sys.argv[1]}'.")

    except (FileNotFoundError, PermissionError) as e:
        exit(f"Error al intentar abrir los archivos. Error: {e}")

    finally:
        print("El programa ha finalizado.")


if __name__ == "__main__":
    main()
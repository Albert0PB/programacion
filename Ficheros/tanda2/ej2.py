"""
2. Escribe un programa que guarde en un fichero el contenido de otros dos ficheros, de tal forma que en el fichero
resultante aparezcan las líneas de los primeros dos ficheros mezcladas, es decir, la primera línea será del primer
fichero, la segunda será del segundo fichero, la tercera será la siguiente del primer fichero, etc.

Los nombres de los dos ficheros origen y el nombre del fichero destino se deben pasar como argumentos en la línea de
comandos.

Hay que tener en cuenta que los ficheros de donde se van cogiendo las líneas pueden tener tamaños diferentes.

Author: Alberto Pérez Bernabeu
"""
import sys


def main():
    if len(sys.argv) != 4 or not all(isinstance(argv, str)for argv in sys.argv[1:]):
        raise ValueError("A este programa se le deben pasar tres argumentos: los nombres de dos ficheros existentes y "
                         "un nombre de fichero de destino.",
                         f"Argumentos pasados: {sys.argv[1:]}")

    try:
        with (open(sys.argv[1], 'r') as file1, open(sys.argv[2], 'r') as file2, open(sys.argv[3], 'w') as output):
            lines1 = file1.readlines()
            lines2 = file2.readlines()

            max_lines = max(len(lines1), len(lines2))

            for i in range(max_lines):
                if i < len(lines1):
                    output.write(lines1[i])
                if i < len(lines2):
                    output.write(lines2[i])

    except (FileNotFoundError, PermissionError) as e:
        exit(f"Error al intentar abrir los archivos. Error: {e}")

    finally:
        print("El programa ha finalizado.")


if __name__ == "__main__":
    main()




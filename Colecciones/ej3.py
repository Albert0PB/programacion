"""
3. Crea un minidiccionario español-inglés que contenga, al menos, 20 palabras (con su correspondiente traducción).
Utiliza un diccionario para almacenar las parejas de palabras. El programa pedirá una palabra en español y dará la
correspondiente traducción en inglés.

Author: Alberto Pérez Bernabeu
"""

spanish_english_dict = {'Si': 'If', 'Mientras': 'While', 'Entorno': 'Environment', 'Programación': 'Programming',
                        'Ciclo': 'Loop', 'Archivo': 'File', 'Pitón': 'Python', 'Directorio': 'Directory',
                        'Proyecto': 'Project', 'Programador': 'Programmer', 'Carpeta': 'Folder', 'Objeto': 'Object',
                        'Punto': 'Point', 'Conjunto': 'Set', 'Lista': 'List', 'Datos': 'Data',
                        'Método': 'Method', 'Función': 'Function', 'Imprimir': 'Print', 'Suprimir': 'Delete'}


def main():
    while True:
        while True:
            word_sph = input('Indique la palabra que desee traducir al inglés (pulse "ENTER" sin escribir nada para '
                             'salir del programa): ')
            if word_sph == '':
                exit('Gracias por utilizar este programa.')
            elif word_sph in spanish_english_dict.keys():
                break
            print('Palabra no reconocida.')
        print(f'"{word_sph}" se dice "{spanish_english_dict[word_sph]}" en inglés.')


if __name__ == "__main__":
    main()

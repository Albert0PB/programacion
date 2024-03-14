"""
4. Realiza un programa que escoja al azar 5 palabras en español del minidiccionario del ejercicio anterior.
El programa irá pidiendo que el usuario teclee la traducción al inglés de cada una de las palabras y comprobará si
son correctas. Al final, el programa deberá mostrar cuántas respuestas son válidas y cuántas erróneas.
"""
from Prog.Trim2.DICTS_SETS import ej3
from random import choice


def main():
    correct_guesses = 0
    incorrect_attempts = 0
    for n in range(5):
        word_to_translate = choice(list(ej3.spanish_english_dict.keys()))
        attempt = input(f'Indique la traducción al inglés de "{word_to_translate}": ')
        if attempt == ej3.spanish_english_dict[word_to_translate]:
            correct_guesses += 1
            print('¡Enhorabuena, has acertado!')
        else:
            incorrect_attempts += 1
            print(f'¡Incorrecto! La respuesta correcta era "{ej3.spanish_english_dict[word_to_translate]}".')
    print(f'\nHas acertado {correct_guesses} veces.\nHas tenido {incorrect_attempts} errores.\n¡Gracias por jugar!')


if __name__ == "__main__":
    main()

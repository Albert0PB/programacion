"""
This program asks for a letter to be introduced, it tells if it's a consonant or a vowel and ends when
a blank space is typed in.

Author: Alberto Pérez Bernabeu

Starting date: 28-10-23
Last modification: 30-10-23
"""

print("Con este programa puedes saber si la letra introducida es vocal o no. Para salir, introduce un espacio "
      "en blanco.")
letter = 0
while True:
    letter = str(input("Introduce la letra:\n"))
    if letter == "":
        print("Fin del programa.")
        break
    elif letter == "a":
        print(f"La letra {letter} es una vocal.")
    elif letter == "e":
        print(f"La letra {letter} es una vocal.")
    elif letter == "i":
        print(f"La letra {letter} es una vocal.")
    elif letter == "o":
        print(f"La letra {letter} es una vocal.")
    elif letter == "u":
        print(f"La letra {letter} es una vocal.")
    elif letter == "A":
        print(f"La letra {letter} es una vocal.")
    elif letter == "E":
        print(f"La letra {letter} es una vocal.")
    elif letter == "I":
        print(f"La letra {letter} es una vocal.")
    elif letter == "O":
        print(f"La letra {letter} es una vocal.")
    elif letter == "U":
        print(f"La letra {letter} es una vocal.")
    else:
        print(f"El carácter introducido, {letter}, no es una vocal.")

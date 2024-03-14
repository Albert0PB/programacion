"""
The program asks for a phrase and counts the number of words in it.

Author: Alberto Pérez Bernabeu

Starting date: 09-11-23
Last modification: 09-11-23
"""

phrase = str(input("Introduzca una oración:\n"))

word_counter = 1

for c in phrase:
    if c == " ":
        word_counter += 1

print(f"En la oración hay {word_counter} palabras.")

"""
Program that asks for a String and converts lower cases in upper cases and vice versa.

Author: Alberto Pérez Bernabeu

Starting date: 09-11-2023
Last modification:
"""

output_string = ""

input_string = str(input("Por favor, introduce una cadena.\n"))

for c in input_string:
    if c.isupper():
        output_string += c.lower()
    elif c.islower():
        output_string += c.upper()
    else:
        output_string += c

print(f"La cadena resultante es: {output_string}")

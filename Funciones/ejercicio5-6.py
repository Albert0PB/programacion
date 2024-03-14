"""
Stick code and morse code functions.

Author: Alberto Pérez Bernabeu

Starting date: 09-12-2023
Last modification: 09-12-2023
"""


def stick_notation(number):
    import ejercicio2
    digits = ejercicio2.digit_count(number)
    output = ""
    for i in range(digits):
        current_digit = ejercicio2.digit_in_position(number, i)
        output += ("|" * current_digit) + " - "
    output = output[0:(len(output) - 2)]
    return output


def int_to_morse(number):
    import ejercicio2
    MORSE_CODES = ["_____", ".____", "..___", "...__", "...._", ".....", "_....", "__...", "___..", "____."]
    digits = ejercicio2.digit_count(number)
    output = ""
    for i in range(digits):
        current_digit = ejercicio2.digit_in_position(number, i)
        output += f"{MORSE_CODES[current_digit]} "
    return output

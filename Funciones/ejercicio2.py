"""
Functions library:
    es_capicúa              X       is_palindrome
    es_primo                X       is_prime
    siguiente_primo         X       next_prime
    dígitos                 X       digit_count
    voltea                  X       alehop
    digito_n                X       digit_in_position
    posición_de_digito      X       position_of_digit
    quita_por_detrás        X       erase_behind
    quita_por_delante       X       erase_front
    pega_por_detrás         X       stick_behind
    pega_por_delante        X       stick_front
    trozo_de_número         X       extract
    junta_números           X       stick_numbers

    ALSO

    menu_display    &
    code_verification
    random_array_generation

Author: Alberto Pérez Bernabeu

Starting date: 03-12-2023
Last modification: 12-12-2023
"""


def is_prime(number):  # is it prime por return true y false. sqrt(). <2 es false; par !=2 false.
    divisor = 2
    is_it_prime = True
    while divisor <= (number // 2) and is_it_prime:
        if (number % divisor) == 0:
            is_it_prime = False
        divisor += 1
    return is_it_prime


def next_prime(number):
    next_one = number + 1
    while not is_prime(next_one):
        next_one += 1
    return next_one


def digit_count(number):
    count = 0
    while number != 0:
        number = number // 10
        count += 1
    return count


def erase_behind(number, digits):
    number = number // (10 ** digits)
    return number


def erase_front(number, digits):
    gap = 10 ** (digit_count(number) - digits)
    front = number // gap
    front *= gap
    number -= front
    return number


def stick_numbers(head_num, tail_num):
    head_num *= (10 ** digit_count(tail_num))
    outcome_num = head_num + tail_num
    return outcome_num


def stick_behind(number, sticky_digit):
    outcome_num = stick_numbers(number, sticky_digit)
    return outcome_num


def stick_front(number, sticky_digit):
    outcome_num = stick_numbers(sticky_digit, number)
    return outcome_num


def position_of_digit(input_number, digit):
    position = 0
    while input_number != 0:
        front_digit = input_number // 10 ** (digit_count(input_number) - 1)
        if front_digit == digit:
            break
        input_number -= front_digit * 10 ** (digit_count(input_number) - 1)
        position += 1
    if input_number == 0:
        position = -1
    return position


def digit_in_position(input_number, position):
    count = 0
    while True:
        if count == position:
            digit = input_number // (10 ** (digit_count(input_number) - 1))
            break
        else:
            input_number = erase_front(input_number, 1)
            count += 1
    return digit


def alehop(input_number):
    number_copy = input_number
    output_number = 0
    digit_control = 1
    while digit_control <= digit_count(input_number):
        next_digit = erase_front(number_copy, (digit_count(number_copy) - 1))
        output_number += next_digit * 10 ** (digit_count(number_copy) - 1)
        number_copy = number_copy // 10
        digit_control += 1
    return output_number


def is_palindrome(number_to_check):
    head = erase_behind(number_to_check, (digit_count(number_to_check) // 2))
    tail = erase_front(number_to_check, (digit_count(number_to_check) // 2))
    if head == alehop(tail):
        return True
    else:
        return False


def extract(input_number, starting_digit, ending_digit):
    input_number = erase_behind(input_number, (digit_count(input_number) - ending_digit - 1))
    input_number = erase_front(input_number, starting_digit)
    return input_number


def menu_display(*options, separation_length=10, decoration="-"):
    if len(options) == 1 and isinstance(options, (list, tuple)):
        options = options[0]
    print(decoration * (len(max(options, key=len)) + separation_length + 4 + digit_count(len(options))))
    for i in range(len(options)):
        print(f"{options[i]:<{len(max(options, key=len))}}", " " * separation_length,
              f"{decoration} {i:^{digit_count(len(options))}} {decoration}", sep="")
    print(decoration * (len(max(options, key=len)) + separation_length + 4 + digit_count(len(options))))


def code_verification(*options_in_menu):
    if len(options_in_menu) == 1 and isinstance(options_in_menu, (list, tuple)):
        options_in_menu = options_in_menu[0]
    while True:
        try:
            option = int(input("Indique el código de la consulta que desea realizar: "))
            if 0 <= option <= len(options_in_menu):
                break
            else:
                print("\nIndique un código válido.")
        except ValueError:
            print("\nAsegúrese de introducir un código numérico válido.")
    return option


def random_array_generation(start, end, numbers_quantity=1):
    from random import randrange
    numbers_array = []
    for i in range(numbers_quantity):
        number = randrange(start, end + 1)
        numbers_array.append(number)
    return numbers_array


"""
OPTIONS = []
OPTIONS.append("Opción Salir")
for i in range(1, 1001):
    OPTIONS.append(f"Opción {i}")
menu_display(OPTIONS)
"""

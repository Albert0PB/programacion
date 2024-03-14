"""
Statistics library.

Author: Alberto Pérez Bernabeu

Starting date: 08-12-2023
Last modification:
"""


def maximum(*numbers):
    if len(numbers) == 1 and isinstance(numbers, (list, tuple)):
        numbers = numbers[0]
    maximum_number = numbers[0]
    for i in range(len(numbers)):
        if numbers[i] > maximum_number:
            maximum_number = numbers[i]
    return maximum_number


def minimum(*numbers):
    if len(numbers) == 1 and isinstance(numbers, (list, tuple)):
        numbers = numbers[0]
    minimum_number = numbers[0]
    for i in range(len(numbers)):
        if numbers[i] < minimum_number:
            minimum_number = numbers[i]
    return minimum_number


def mean(*numbers):
    if len(numbers) == 1 and isinstance(numbers, (list, tuple)):
        numbers = numbers[0]
    total_sum = 0
    for i in range(len(numbers)):
        total_sum += numbers[i]
    numbers_mean = total_sum / len(numbers)
    return numbers_mean


def variance(*numbers):
    if len(numbers) == 1 and isinstance(numbers, (list, tuple)):
        numbers = numbers[0]
    variance_sum = 0
    for i in range(len(numbers)):
        variance_sum += ((numbers[i] - mean(numbers)) ** 2) / (len(numbers) - 1)
    return variance_sum


def median(*numbers):
    if len(numbers) == 1 and isinstance(numbers, (list, tuple)):
        numbers = numbers[0]
    numbers_array = []
    for i in range(len(numbers)):
        numbers_array.append(numbers[i])
    for i in range(len(numbers_array) - 1):
        if numbers_array[i] > numbers_array[i + 1]:
            holder = numbers_array[i]
            numbers_array[i] = numbers_array[i + 1]
            numbers_array[i + 1] = holder
    median_number = numbers_array[(len(numbers_array) // 2)]
    return median_number


# print(mode(1, 1, 1, 1, 2, 1, 5, 1, 8, 8, 2))

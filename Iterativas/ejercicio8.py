"""
Program that shows a chronometer.

Author: Alberto Pérez Bernabeu

Starting date: 28-10-23
Last modification: 06-11-23
"""
from time import sleep

print("Este programa iniciará un cronómetro cuando lo indique. El cronómetro marca como máximo un día y se reinicia.\n")

seconds = 55
minutes = 59
hours = 23

while True:
    start = int(input("Introduzca el número 0 para comenzar el cronómetro.\n"))
    if start == 0:
        break

while start == 0:
    sleep(1)
    seconds += 1
    print(f"{hours:02}:{minutes:02}:{seconds:02}")
    if seconds == 59:
        seconds = -1
        minutes += 1
        if minutes == 59:
            seconds = -1
            minutes = -1
            hours += 1
            if hours == 24:
                seconds = 0
                minutes = 0
                hours = 0

"""
Very cool program about grades. (v2.0)

Author: Alberto Pérez Bernabeu

Starting date: 21-11-2023
Last modification: 04-12-2023
"""
from sys import exit

MODULES = ["PROGRAMACIÓN", "LENGUAJE DE MARCAS", "BASES DE DATOS", "SISTEMAS INFORMÁTICOS"]
students = []

print("\nBienvenido. En este programa puede introducir información sobre los alumnos de 1º de DAW en el IES Gran "
      "Capitán y realizar consultas sobre los datos almacenados.\n")

print("En primer lugar, debe introducir los nombres y apellidos de los alumnos (se recomienda que utilice el mismo "
      "formato en la introducción de los nombres para conservar la claridad en las consultas).\n")

name_order = 1
while True:
    name = input(f"Introduzca nombre y apellidos del alumno {name_order} (si desea dejar de introducir datos, pulse "
                 f"'ENTER' sin escribir nada):\n")
    if name == "":
        break
    name_order += 1
    students.append(name)

print("\nA continuación, se le pedirá que introduzca las calificaciones de los alumnos en cada una de las "
      "asignaturas\n")

grades_matrix = []
for i in range(len(students)):
    student_grades = []
    for j in range(len(MODULES)):
        while True:
            try:
                grade = float(input(f"\nIntroduzca la nota de {students[i]} para la asignatura de {MODULES[j]}: "))
                if 0 <= grade <= 10:
                    student_grades.append(grade)
                    break
                else:
                    print("\nAsegúrese de introducir una calificación entre 0 y 10.")
            except ValueError:
                print("\nAsegúrese de introducir un valor numérico entre 0 y 10.")
    grades_matrix.append(student_grades)

while True:
    print("\n\nA continuación, usted puede escoger el tipo de consulta.")
    print("\n---------------------------------------------------------------")
    print("Consulta de las calificaciones del curso completo         || 0 \n"
          "Consulta de las calificaciones de un alumno en concreto   || 1 \n"
          "Consulta de la nota media de un módulo                    || 2 \n"
          "Consulta de la nota máxima en un módulo                   || 3 \n"
          "Consulta de la nota mínima en un módulo                   || 4 \n"
          "Lista descendente de las calificaciones de un módulo      || 5 \n"
          "Salir del programa                                        || 6")
    print("---------------------------------------------------------------\n")

    while True:
        try:
            option = int(input("Indique el código de la consulta que desea realizar: "))
            if 0 <= option <= 6:
                break
            else:
                print("\nIndique un código válido.")
        except ValueError:
            print("\nAsegúrese de introducir un código numérico válido.")

    if option == 6:
        print("Gracias por utilizar el programa.")
        exit()

    if option == 0:
        print("")
        print(" " * 30, sep="", end="")
        for i in range(len(MODULES)):
            print("|", f"{MODULES[i]:^25s}", "|", end="")
        print("")
        for i in range(len(students)):
            print(f"{students[i]:<30s}", end="")
            for j in range(len(MODULES)):
                print("|", f"{grades_matrix[i][j]:^25.2f}", "|", end="")
            print("")

    elif option == 1:
        print("\nA continuación, especifíque el alumno cuyas calificaciones desea consultar.\n")
        for i in range(len(students)):
            print(f"{students[i]:<30s}", " " * 2, "| ", i, sep="")

        while True:
            try:
                consult_1_student_code = int(input("\nIntroduzca el código del alumno: "))
                if 0 <= consult_1_student_code <= len(students):
                    break
                else:
                    print("\nAsegúrese de introducir un código correcto.")
            except ValueError:
                print("\nAsegúrese de introducir un código numérico correcto.")

        print("")
        print(" " * 30, sep="", end="")
        for i in range(len(MODULES)):
            print("|", f"{MODULES[i]:^25s}", "|", end="")
        print("")
        print(f"{students[consult_1_student_code]:<30s}", end="")
        for i in range(len(MODULES)):
            print("|", f"{grades_matrix[consult_1_student_code][i]:^25.2f}", "|", end="")

    elif option == 2:
        print("\nA continuación, especifíque el módulo cuya nota media desea consultar.\n")
        for i in range(len(MODULES)):
            print(f"{MODULES[i]:<25s}", " " * 2, "| ", i, sep="")

        while True:
            try:
                consult_2_module_code = int(input("\nIntroduzca el código del módulo: "))
                if 0 <= consult_2_module_code <= len(MODULES):
                    break
                else:
                    print("\nAsegúrese de introducir un código correcto.")
            except ValueError:
                print("\nAsegúrese de introducir un código numérico correcto.")

        total_sum = 0
        for i in range(len(students)):
            total_sum += grades_matrix[i][consult_2_module_code]
        print(f"\nLa nota media en el módulo {MODULES[consult_2_module_code]} es: {total_sum / len(students)}.")

    elif option == 3:
        print("\nA continuación, especifíque el módulo cuya nota máxima desea consultar.\n")
        for i in range(len(MODULES)):
            print(f"{MODULES[i]:<25s}", " " * 2, "| ", i, sep="")

        while True:
            try:
                consult_3_module_code = int(input("\nIntroduzca el código del módulo: "))
                if 0 <= consult_3_module_code <= len(MODULES):
                    break
                else:
                    print("\nAsegúrese de introducir un código correcto.")
            except ValueError:
                print("\nAsegúrese de introducir un código numérico correcto.")

        consult_3_grades_list = []
        for i in range(len(students)):
            consult_3_grades_list.append(grades_matrix[i][consult_3_module_code])
        for i in range(len(consult_3_grades_list)):
            if consult_3_grades_list[i] == max(consult_3_grades_list):
                print(f"\nPara el módulo {MODULES[consult_3_module_code]}, la nota máxima es "
                      f"{max(consult_3_grades_list)}, obtenida por el alumno {students[i]}")

    elif option == 4:
        print("\nA continuación, especifíque el módulo cuya nota mínima desea consultar.\n")
        for i in range(len(MODULES)):
            print(f"{MODULES[i]:<25s}", " " * 2, "| ", i, sep="")

        while True:
            try:
                consult_4_module_code = int(input("\nIntroduzca el código del módulo: "))
                if 0 <= consult_4_module_code <= len(MODULES):
                    break
                else:
                    print("\nAsegúrese de introducir un código correcto.")
            except ValueError:
                print("\nAsegúrese de introducir un código numérico correcto.")

        consult_4_grades_list = []
        for i in range(len(students)):
            consult_4_grades_list.append(grades_matrix[i][consult_4_module_code])
        for i in range(len(consult_4_grades_list)):
            if consult_4_grades_list[i] == min(consult_4_grades_list):
                print(f"\nPara el módulo {MODULES[consult_4_module_code]}, la nota mínima es "
                      f"{min(consult_4_grades_list)}, obtenida por el alumno {students[i]}")

    elif option == 5:
        print("\nA continuación, especifíque el módulo sobre el cuál desea generar un listado descendente de las "
              "calificaciones obtenidas por los alumnos..\n")
        for i in range(len(MODULES)):
            print(f"{MODULES[i]:<25s}", " " * 2, "| ", i, sep="")

        while True:
            try:
                consult_5_module_code = int(input("\nIntroduzca el código del módulo: "))
                if 0 <= consult_5_module_code <= len(MODULES):
                    break
                else:
                    print("\nAsegúrese de introducir un código correcto.")
            except ValueError:
                print("\nAsegúrese de introducir un código numérico correcto.")

        consult_5_grades_list = []
        for i in range(len(students)):
            consult_5_grades_list.append(grades_matrix[i][consult_5_module_code])

        order_protector = 0
        names_juggler = 0
        names_5_consult = students.copy()
        for i in range(len(consult_5_grades_list) - 1):
            if consult_5_grades_list[i] < consult_5_grades_list[i + 1]:
                order_protector = consult_5_grades_list[i]
                consult_5_grades_list[i] = consult_5_grades_list[i + 1]
                consult_5_grades_list[i + 1] = order_protector

                names_juggler = names_5_consult[i]
                names_5_consult[i] = names_5_consult[i + 1]
                names_5_consult[i + 1] = names_juggler

        print("")
        for i in range(len(names_5_consult)):
            print(f"{names_5_consult[i]:<30s}", " " * 2, f"| {consult_5_grades_list[i]}", sep="")


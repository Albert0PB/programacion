"""
Even cooler program about grades. (v3.0)

Author: Alberto Pérez Bernabeu

Starting date: 21-11-2023
Last modification: 04-12-2023
"""


def main():
    from sys import exit
    import functions

    MODULES = ["PROGRAMACIÓN", "LENGUAJE DE MARCAS", "BASES DE DATOS", "SISTEMAS INFORMÁTICOS"]
    students = []

    print("\nBienvenido. En este programa puede introducir información sobre los alumnos de 1º de DAW en el IES Gran "
          "Capitán y realizar consultas sobre los datos almacenados.\n")

    print("En primer lugar, debe introducir los nombres y apellidos de los alumnos (se recomienda que utilice el mismo "
          "formato en la introducción de los nombres para conservar la claridad en las consultas).\n")

    grades_matrix = []
    name_order = 1
    while True:
        name = input(
            f"\nIntroduzca nombre y apellidos del alumno {name_order} (si desea dejar de introducir datos, pulse "
            f"'ENTER' sin escribir nada):\n")
        if name == "":
            break

        student_grades = []
        for j in range(len(MODULES)):
            while True:
                try:
                    grade = float(input(f"\nIntroduzca la nota de {name} para la asignatura de {MODULES[j]}: "))
                    if 0 <= grade <= 10:
                        student_grades.append(grade)
                        break
                    else:
                        print("\nAsegúrese de introducir una calificación entre 0 y 10.")
                except ValueError:
                    print("\nAsegúrese de introducir un valor numérico entre 0 y 10.")

        grades_matrix.append(student_grades)
        name_order += 1
        students.append(name)

    print("\nA continuación, se le pedirá que introduzca las calificaciones de los alumnos en cada una de las "
          "asignaturas\n")

    CONSULTS = ["Consulta de las calificaciones del curso completo",
                "Consulta de las calificaciones de un alumno en concreto",
                "Consulta de la nota media de un módulo", "Consulta de la nota máxima en un módulo",
                "Consulta de la nota mínima en un módulo", "Lista descendente de las calificaciones de un módulo",
                "Salir del programa"]

    while True:
        print("")
        functions.menu_display(CONSULTS, decoration_length=70)

        option = functions.code_verification(CONSULTS)

        if option == 6:
            print("Gracias por utilizar el programa.")
            exit()

        elif option == 0:
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
            functions.menu_display(students)

            consult_1_student_code = functions.code_verification(students)

            print("")
            print(" " * 30, sep="", end="")
            for i in range(len(MODULES)):
                print("|", f"{MODULES[i]:^25s}", "|", end="")
            print("")
            print(f"{students[consult_1_student_code]:<30s}", end="")
            for i in range(len(MODULES)):
                print("|", f"{grades_matrix[consult_1_student_code][i]:^25.2f}", "|", end="")

        elif option == 2:
            functions.menu_display(MODULES)

            consult_2_module_code = functions.code_verification(MODULES)

            total_sum = 0
            for i in range(len(students)):
                total_sum += grades_matrix[i][consult_2_module_code]
            print(f"\nLa nota media en el módulo {MODULES[consult_2_module_code]} es: {total_sum / len(students)}.")

        elif option == 3:
            functions.menu_display(MODULES)

            consult_3_module_code = functions.code_verification(MODULES)

            consult_3_grades_list = []
            for i in range(len(students)):
                consult_3_grades_list.append(grades_matrix[i][consult_3_module_code])
            for i in range(len(consult_3_grades_list)):
                if consult_3_grades_list[i] == max(consult_3_grades_list):
                    print(f"\nPara el módulo {MODULES[consult_3_module_code]}, la nota máxima es "
                          f"{max(consult_3_grades_list)}, obtenida por el alumno {students[i]}")

        elif option == 4:
            functions.menu_display(MODULES)

            consult_4_module_code = functions.code_verification(MODULES)

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

            functions.menu_display(MODULES)

            consult_5_module_code = functions.code_verification(MODULES)

            consult_5_grades_list = []
            for i in range(len(students)):
                consult_5_grades_list.append(grades_matrix[i][consult_5_module_code])

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


if __name__ == "__main__":
    main()

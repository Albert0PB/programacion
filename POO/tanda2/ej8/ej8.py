"""
Muestra un menú con las siguientes opciones:

Introducir (por teclado) una fecha pidiendo por teclado año, mes y día en formato dd/mm/aaaa. Si no se introduce
correctamente se devuelve un mensaje de error. Usa una función booleana para validar la fecha.

Añadir días a la fecha. Pide un número de días para sumar a la fecha introducida previamente y actualiza su valor.

Si el número es negativo restará los días. Esta opción sólo podrá realizarse si hay una fecha introducida (se ha
ejecutado la opción anterior), si no la hay mostrará un mensaje de error.

Añadir meses a la fecha. El mismo procedimiento que la opción anterior.

Añadir años a la fecha. El mismo procedimiento que la opción 2.

Comparar la fecha introducida con otra. Pide una fecha al usuario en formato dd/mm/aaaa (válida, si no lo es da error)
y la comparará con la que tenemos guardada, posteriormente mostrará si esta fecha es anterior, igual o posterior a la
que tenemos almacenada y el número de días comprendido entre las dos fechas.

Mostrar la fecha en formato largo (palabras: "lunes, 1 de febrero de 2021").

Terminar.

Consideraciones a tener en cuenta:

El menú lo hacemos con una clase a la que llamaremos Menú, esa clase permitirá ir añadiendo opciones y escoger
alguna opción.

Las fechas las manejaremos con la clase datetime.date.
"""
from menu import Menu
from datetime import date, timedelta, datetime
from dateutil.relativedelta import relativedelta
import locale

locale.setlocale(locale.LC_ALL, 'es_ES')

date_ = None


def terminate():
    print('Gracias por utilizar este programa.')
    exit(0)


def date_input():
    raw_date = input('Indique una fecha en formato dd/mm/aaaa: ')
    return date(int(raw_date[6:]), int(raw_date[3:5]), int(raw_date[0:2]))


def assign_date():
    global date_
    date_ = date_input()


def days_input():
    return int(input('Indique un número entero de días para sumar (si quiere restar días, '
                     'indique un número negativo): '))


def add_days():
    global date_
    if date_ is None:
        print('No se ha introducido ninguna fecha antes de seleccionar la suma de días.')
        return
    days_to_add = days_input()
    date_ += timedelta(days=days_to_add)


def months_input():
    return int(input('Indique un número entero de meses para sumar (si quiere restar meses, '
                     'indique un número negativo): '))


def add_months():
    global date_
    if date_ is None:
        print('No se ha introducido ninguna fecha antes de seleccionar la suma de meses.')
        return
    months_to_add = months_input()
    date_ += relativedelta(months=months_to_add)


def years_input():
    return int(input('Indique un número entero de años para sumar (si quiere restar años, '
                     'indique un número negativo): '))


def add_years():
    global date_
    if date_ is None:
        print('No se ha introducido ninguna fecha antes de seleccionar la suma de años.')
        return
    years_to_add = years_input()
    date_ += relativedelta(years=years_to_add)


def compare_date():
    global date_
    if date_ is None:
        raise ValueError('No se ha introducido ninguna fecha en el programa.')
    other_date = date_input()
    if other_date > date_:
        print(f'{other_date} es posterior a {date_}.')
    elif other_date < date_:
        print(f'{other_date} es anterior a {date_}.')
    else:
        print('Ambas son la misma fecha.')


def show_date():
    global date_
    if date_ is None:
        raise ValueError('No existe ninguna fecha introducida.')
    dt = datetime(year=date_.year, month=date_.month, day=date_.day)
    print(dt.strftime('%A, %d de %B de %Y'))


def main():
    menu1 = Menu('Terminar', 'Introducir fecha', 'Añadir días', 'Añadir meses', 'Añadir años', 'Comparar fecha',
                 'Mostrar fecha')

    while True:
        selected = menu1.pick_option()

        match selected:
            case 0:
                terminate()
            case 1:
                assign_date()
            case 2:
                add_days()
            case 3:
                add_months()
            case 4:
                add_years()
            case 5:
                compare_date()
            case 6:
                show_date()
        

if __name__ == "__main__":
    main()

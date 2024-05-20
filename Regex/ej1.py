"""
1. Programa que recibe dos parámetros: un fichero de texto y una cadena que le indica qué información va a extraer del
mismo, después muestra por la pantalla los datos extraídos.

Los posibles valores del segundo parámetro y la información que extrae es:

    DNI: extrae los DNI.
    IP: extrae las direcciones IP.
    MAT: extrae matrículas de coche con formato 0000XXX.
    HEX: extrae números hexadecimales. Entendemos que las letras entre A y F son en mayúsculas y el número empieza
    con #.
    FEC: extrae fechas con formato dd/mm/aaaa.
    TWT: extrae usuarios de twitter: empieza por @ y puede contener letras mayúsculas y minúsculas, números, guiones y
    guiones bajos.

El programa tiene que ser en relación a su complejidad y número de líneas lo más eficiente posible.

Author: Alberto Pérez Bernabeu
Starting date: 16/5/2024
Last modification: 18/5/2024
"""
import re

regexps = {
    'DNI': r'\d{8}\-?\w',
    'IP': r'((25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9][0-9]|[1-9]|(0))\.){3}(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]['
          r'0-9]|[1-9]|(0))',
    'MAT': r'\d{4}\w{3}', 'HEX': r'\#[0-9A-F]',
    'FEC': r'(0[1-9]|[12][0-9]|3[01])/(0[1-9]|1[0-2])/\d{4}',
    'TWT': r'\@[a-zA-Z0-9\-\_]*'}

file_text = str(open('archivo1', 'r').read())


def main():
    print('DNI encontrados:', re.findall(regexps['DNI'], file_text))
    print('IP encontradas:', re.findall(regexps['IP'], file_text))  # No funciona correctamente
    print('MAT encontrados:', re.findall(regexps['MAT'], file_text))
    print('HEX encontrados:', re.findall(regexps['HEX'], file_text))
    print('FEC encontrados:', re.findall(regexps['FEC'], file_text))  # No funciona correctamente
    print('TWT encontrados:', re.findall(regexps['TWT'], file_text))


if __name__ == "__main__":
    main()

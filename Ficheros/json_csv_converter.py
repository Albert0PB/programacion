"""
Ejercicios que hay traer hechos mañana:

1. Utilidad: conversor de CSV a JSON

Recibe como parámetro un CSV (un argumento con extensión .csv)
Si no recibe esto, error

Resultado es un fichero JSON con el mismo nombre pero con extensión JSON

--> csv2json

2. Utilidad: conversor de JSON a CSV

Recibe como parámetro un JSON (un argumento con extensión .json)
Si no recibe esto, error

Resultado es un fichero CSV con el mismo nombre pero con extensión csv

--> json2csv

Author: Alberto Pérez Bernabeu
"""
import pandas as pd
import os

csv_file = 'C:/Users/Alber/PycharmProjects/repo/Ficheros/utils/peliculas.csv'
json_file = 'C:/Users/Alber/PycharmProjects/repo/Ficheros/utils/libros.json'


class FileExtensionError(BaseException):
    def __init__(self, extension_required, extension_received):
        super().__init__(f"¡Error! Extensión de fichero no soportada."
                         f"[Extensión requerida: '{extension_required}']"
                         f"[Extensión recibida: '{extension_received}']")
        self.extension_required = extension_required
        self.extension_received = extension_received


def json_to_csv(file):
    output_file_extension = '.csv'
    df = pd.read_json(file)
    filename, file_extension = os.path.splitext(file)
    if file_extension != '.json':
        raise FileExtensionError('.json', file_extension)
    output_file = filename + output_file_extension
    df.to_csv(output_file, index=False)


def csv_to_json(file):
    output_file_extension = '.json'
    df = pd.read_csv(file)
    filename, file_extension = os.path.splitext(file)
    if file_extension != '.csv':
        raise FileExtensionError('.csv', file_extension)
    output_file = filename + output_file_extension
    df.to_json(output_file, orient='records')


def main():
    json_to_csv(json_file)
    csv_to_json(csv_file)


if __name__ == "__main__":
    main()

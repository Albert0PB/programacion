"""
Crea una clase que represente una estructura de datos tipo pila (stack) y otra de tipo cola (queue).

La pila y la cola permitirán estas operaciones:

    - Crear la pila o la cola con o sin valores iniciales o a partir de otra cola o pila.
    - Obtener el número de elementos almacenados (tamaño).
    - Saber si la pila o la cola está vacía.
    - Vaciar completamente la pila o la cola.

Para el caso de la pila:

    - Apilar (push): se añade un elemento a la pila. Se añade al principio de esta.
    - Desapilar (pop): se saca (debe devolverse) un elemento de la pila y se elimina.
    - Leer el elemento superior de la pila sin retirarlo (top).

Para el caso de la cola:

    - Encolar (enqueue): se añade un elemento a la cola. Se añade al final de esta.
    - Desencolar (dequeue): se saca (debe devolverse) y se elimina el elemento frontal de la cola, es decir, el primer
      elemento que entró.
    - Leer el elemento frontal de la cola, es decir, el primer elemento que entró, sin retirarlo (front).
"""
from __future__ import annotations
from typeguard import typechecked
from abc import ABC
from typing import Union


class DataStructure(ABC):

    def size(self):
        pass

    def is_empty(self):
        pass

    def clear(self):
        pass


@typechecked
class Stack(DataStructure):
    def __init__(self, *data):
        if len(data) == 1:
            if isinstance(data, Union[list, tuple]):
                self.__data = (list(data)).copy()
            elif isinstance(data, Union[Stack, Queue]):
                self.__data = list(data.data).copy()

        elif len(data) > 1 or (len(data) == 1 and not isinstance(data, Union[list, tuple, Stack, Queue])):
            self.__data = list(data)

    @property
    def data(self):
        return self.__data

    @property
    def size(self):
        return len(self.data)

    def is_empty(self):
        if self.size > 0:
            return False
        else:
            return True

    def clear(self):
        self.__data = []

    def push(self, value):
        self.data.append(value)

    def pop(self):
        print(self.data[len(self.__data) - 1])
        self.__data.pop(len(self.data) - 1)

    def top(self):
        return self.__data[len(self.__data) - 1]


class Queue(DataStructure):
    def __init__(self, *data):
        if len(data) == 1:
            if isinstance(data, Union[list, tuple]):
                self.__data = list(data).copy()
            elif isinstance(data, Union[Stack, Queue]):
                self.__data = list(data.data).copy()
        elif len(data) > 1 or (len(data) == 1 and not isinstance(data, Union[list, tuple, Stack, Queue])):
            self.__data = list(data)

    @property
    def data(self):
        return self.__data

    @property
    def size(self):
        return len(self.data)

    def is_empty(self):
        if self.size > 0:
            return False
        else:
            return True

    def clear(self):
        self.__data = []

    def enqueue(self, value):
        self.data.append(value)

    def dequeue(self):
        print(self.data[len(self.__data) - 1])
        self.__data.pop(0)

    def front(self):
        return self.__data[0]


def main():
    pass


if __name__ == "__main__":
    main()

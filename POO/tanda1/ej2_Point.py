"""
Implementa una clase Point con sus atributos x e y. La clase debe contener: su constructor, los getters y setters
(propiedades), un invert_coordinates() que invierta las coordenadas x e y del punto. Además, la clase debe tener un
__str__() para poder imprimir los puntos en formato “(x,y)”. Implementa un test donde crees un punto, lo imprimas
utilizando de manera implícita el método __str__(), imprimas su coordenada x, asignes 0 a su coordenada x, y vuelvas a
imprimir el punto.
"""


class Point:
    def __init__(self, x, y):
        self.__x = x
        self.__y = y

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        self.__y = value

    def invert_coords(self):
        swapper = self.__x
        self.__x = self.__y
        self.__y = swapper

    def __str__(self):
        return f"({self.__x}, {self.__y})"


def main():
    point1 = Point(2, 3)
    print(point1)
    print(point1.x)
    point1.x = 0
    print(point1)


if __name__ == "__main__":
    main()

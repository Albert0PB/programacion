"""
Implementa la clase Rectangulo (determinado por dos objetos Point) que además de su constructor, tendrá dos métodos
para calcular su área y su perímetro que tienes que transformar en propiedades. Implementa también un test que cree
dos puntos y un rectángulo a partir de estos dos puntos y que muestre el área y perímetro de dicho rectángulo.
"""
from ej2_Point import Point
from typeguard import typechecked


@typechecked
class Rectangle:
    def __init__(self, point1: Point, point2: Point):
        self.__point1 = point1
        self.__point2 = point2

    @property
    def area(self):
        return abs((self.__point1.x - self.__point2.x) * (self.__point1.y - self.__point2.y))

    @property
    def perimeter(self):
        return abs(2 * (self.__point1.x - self.__point2.x) + 2 * (self.__point1.y - self.__point2.y))


def main():
    p1 = Point(10, 20)
    p2 = Point(5, 37)
    rect = Rectangle(p1, p2)

    print(rect.area)
    print(rect.perimeter)


if __name__ == "__main__":
    main()

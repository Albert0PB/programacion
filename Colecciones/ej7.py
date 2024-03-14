"""
7. Una empresa de venta por internet de productos electrónicos nos ha encargado implementar un carrito de la compra.
Crea la clase Carrito. Al carrito se le pueden ir agregando elementos que se guardarán en una lista, por tanto,
deberás crear la clase Elemento. Cada elemento del carrito deberá contener el nombre del producto, su precio y la
cantidad (número de unidades de dicho producto). A continuación se muestra tanto el contenido del programa principal
como la salida que debe mostrar el programa. Los métodos a implementar se pueden deducir del programa principal.

Contenido del programa principal:


Salida:

Contenido del carrito
=====================
Tarjeta SD 64Gb PVP: 19,95 Unidades: 2 Subtotal: 39,90
Canon EOS 2000D PVP: 449,00 Unidades: 1 Subtotal: 449,00
Hay 2 productos en la cesta.
El total asciende a 488,90 euros
Continúa la compra...
Contenido del carrito
=====================
Tarjeta SD 64Gb PVP: 19,95 Unidades: 2 Subtotal: 39,90
Canon EOS 2000D PVP: 449,00 Unidades: 1 Subtotal: 449,00
Samsung Galaxy Tab PVP: 199,00 Unidades: 3 Subtotal: 597,00
Tarjeta SD 64Gb PVP: 19,95 Unidades: 1 Subtotal: 19,95
Ahora hay 4 productos en la cesta.
El total asciende a 1105,85 euros

Author: Alberto Pérez Bernabeu
"""
from __future__ import annotations
from typeguard import typechecked


@typechecked
class Carrito:
    def __init__(self):
        self.__elementos = []

    @property
    def numero_elementos(self):
        return len(self.__elementos)

    @property
    def importe_total(self):
        total_amount = 0
        for price in self.__elementos:
            total_amount += price.partial
        return total_amount

    def agrega(self, item: Elemento):
        self.__elementos.append(item)

    def __str__(self):
        carrito_string = 'CONTENIDO DEL CARRITO\n====================='
        for item in self.__elementos:
            carrito_string += f'\n{item}'
        return carrito_string


@typechecked
class Elemento:
    def __init__(self, name: str, price_in_euros: float, quantity: int):
        self.__name = name
        self.__price_in_euros = price_in_euros
        self.__quantity = quantity

    @property
    def partial(self):
        return self.__quantity * self.__price_in_euros

    def __str__(self):
        return (f'{self.__name} PVP: {self.__price_in_euros:.2f} € Unidades: {self.__quantity} '
                f'Subtotal: {self.partial:.2f} €')


def main():
    mi_carrito = Carrito()
    mi_carrito.agrega(Elemento("Tarjeta SD 64Gb", 19.95, 2))
    mi_carrito.agrega(Elemento("Canon EOS 2000D", 449, 1))
    print(mi_carrito)
    print(f"Hay {mi_carrito.numero_elementos} productos en la cesta.")
    print(f"El total asciende a {mi_carrito.importe_total:.2f}  euros")

    print("\nContinúa la compra...\n")
    mi_carrito.agrega(Elemento("Samsung Galaxy Tab", 199, 3))
    mi_carrito.agrega(Elemento("Tarjeta SD 64Gb", 19.95, 1))
    print(mi_carrito)
    print(f"Ahora hay {mi_carrito.numero_elementos} productos en la cesta.")
    print(f"El total asciende a {mi_carrito.importe_total:.2f}  euros")


if __name__ == "__main__":
    main()

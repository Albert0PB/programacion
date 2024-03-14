"""
8. Mejora el programa anterior (en otro diferente) de tal forma que al intentar agregar un elemento al carrito, se
compruebe si ya existe el producto y, en tal caso, se incremente el número de unidades sin añadir un nuevo elemento.
Observa que en el programa anterior, se repetía el producto “Tarjeta SD 64Gb” dos veces en el carrito. En esta nueva
versión ya no sucede esto, sino que se incrementa el número de unidades del producto que se agrega. El contenido del
programa principal es idéntico al ejercicio anterior.

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
Tarjeta SD 64Gb PVP: 19,95 Unidades: 3 Subtotal: 59,85
Canon EOS 2000D PVP: 449,00 Unidades: 1 Subtotal: 449,00
Samsung Galaxy Tab PVP: 199,00 Unidades: 3 Subtotal: 597,00
Ahora hay 3 productos en la cesta.
El total asciende a 1105,85 euros
"""
from __future__ import annotations
from typeguard import typechecked


@typechecked
class Carrito:
    def __init__(self):
        self.__items = []
        self.__elementos_quantity = {}
        self.__elementos_prices = {}

    @property
    def numero_elementos(self):
        return len(self.__items)

    @property
    def importe_total(self):
        total_amount = 0
        for item in self.__elementos_quantity.keys():
            total_amount += self.__elementos_quantity[item] * self.__elementos_prices[item]
        return total_amount

    def agrega(self, item: Elemento):
        if item.name not in self.__elementos_quantity.keys():
            self.__elementos_quantity.update({item.name: item.quantity})
            self.__elementos_prices.update({item.name: item.price_in_euros})
            self.__items.append(item)
        else:
            self.__elementos_quantity.update({item.name: self.__elementos_quantity[item.name] + item.quantity})
            #  TODO: la cantidad del producto no se actualiza; los subtotales son incorrectos aunque el total está bien

    def __str__(self):
        carrito_string = 'CONTENIDO DEL CARRITO\n====================='
        for item in self.__items:
            carrito_string += f'\n{item}'
        return carrito_string


@typechecked
class Elemento:
    def __init__(self, name: str, price_in_euros: float, quantity: int):
        self.__name = name
        self.__price_in_euros = price_in_euros
        self.__quantity = quantity

    @property
    def name(self):
        return self.__name

    @property
    def quantity(self):
        return self.__quantity

    @property
    def price_in_euros(self):
        return self.__price_in_euros

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

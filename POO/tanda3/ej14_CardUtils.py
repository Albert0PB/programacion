"""
14. Crea en Python las siguientes clases:

Card que simule una carta de naipes. Un naipe tiene un palo (de un conjunto de palos) y un valor
(de un conjunto de valores).

CardPlayer que simule un jugador de naipes. Un jugador tiene un conjunto de naipes.
    - Puede robar una carta de una baraja. Una vez robada el jugador tiene una carta más y la baraja una menos.
    - Puede deshacerse de una carta.
    - Puede recibir cartas.

Deck que simula un conjunto de cartas de naipes.
    - Inicialmente, tiene las cartas que le llegan con el constructor.
    - Puede repartir un conjunto de cartas a un jugador. En la baraja dejan de existir esas cartas.
    - Le pueden quitar la primera carta (robar).
    - Puede barajarse.

Baraja Española e Inglesa (SpanishDeck e EnglishDeck) que heredan de Deck.
"""
from __future__ import annotations
from typeguard import typechecked
from random import choice
from abc import ABC


def check_positive(value):
    if value >= 0:
        return True
    return False


@typechecked
class Card:

    __slots__ = ['__trump', '__value']

    def __init__(self, trump: str, value: str):
        self.__trump = trump
        self.__value = value

    @property
    def trump(self):
        return self.__trump

    @property
    def value(self):
        return self.__value

    def __str__(self):
        return f'{self.__value} de {self.__trump}'


@typechecked
class CardPlayer:
    def __init__(self, *cards: Card):  # List[Card]
        self.__hand = list(cards)

    def take_card_from_deck(self, playing_deck: Deck):
        self.__hand.append(playing_deck.give_top_card())

    def steal_card_from_opponent(self, other: CardPlayer):
        self.__hand.append(other.__hand.pop(choice(range(len(other.__hand)))))

    def discard(self):
        self.display_hand()
        selected_card = int(input('Indique la carta de la que desea descartarse: '))
        self.__hand.pop(selected_card - 1)

    def display_hand(self):
        for index, card in enumerate(self.__hand):
            print(f'{index + 1}- {card}')

    @property
    def hand(self):
        return self.__hand.copy()


@typechecked
class Deck(ABC):
    def __init__(self, cards: list[Card]):
        self.__playing_cards = cards

    @property
    def playing_cards(self):
        return self.__playing_cards

    def deal(self, number_of_cards_to_deal: int):  # TODO: jugador como parámetro
        if not check_positive(number_of_cards_to_deal):
            raise ValueError('Debe indicar una cantidad positiva.')
        cards_to_deal = []
        for i in range(number_of_cards_to_deal):
            cards_to_deal.append(self.give_top_card())
        return cards_to_deal

    def shuffle(self):
        shuffled_deck = []
        while len(self.__playing_cards) > 0:
            shuffled_deck.append(self.__playing_cards.copy().pop(choice(range(len(self.__playing_cards)))))
        self.__playing_cards = shuffled_deck

    def give_top_card(self):
        return self.__playing_cards.pop()


@typechecked
class SpanishDeck(Deck):

    @staticmethod
    def __spanish_cards_creator():
        spanish_trumps = ('Bastos', 'Oros', 'Espadas', 'Copas')
        spanish_values = ('Dos', 'Tres', 'Cuatro', 'Cinco', 'Seis', 'Siete', 'Sota', 'Caballo', 'Rey', 'As')
        return [Card(i, j) for i in spanish_trumps for j in spanish_values].copy()

    def __init__(self):
        super().__init__(SpanishDeck.__spanish_cards_creator())


@typechecked
class EnglishDeck(Deck):

    @staticmethod
    def __english_cards_creator():
        english_trumps = ('Picas', 'Corazones', 'Tréboles', 'Diamantes')
        english_values = ('Dos', 'Tres', 'Cuatro', 'Cinco', 'Seis', 'Siete', 'Ocho', 'Nueve', 'Diez',
                          'Jack', 'Dama', 'Rey', 'As')
        return [Card(i, j) for i in english_trumps for j in english_values]

    def __init__(self):
        super().__init__(EnglishDeck.__english_cards_creator())


def main():
    pass


if __name__ == "__main__":
    pass

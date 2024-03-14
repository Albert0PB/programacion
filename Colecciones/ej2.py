"""
2. Realiza un programa que escoja al azar 10 cartas de la baraja española (10 objetos de la clase Carta). Emplea una
lista para almacenarlas y asegúrate de que no se repite ninguna. Las cartas se deben mostrar ordenadas. Primero se
ordenarán por palo (bastos, copas, espadas, oros) y cuando coincida el palo, se ordenará por número:
as, 2, 3, 4, 5, 6, 7, sota, caballo, rey.

Author: Alberto
"""
from Prog.Trim2.OOP.tanda3.ej14_CardUtils import SpanishDeck
from random import choice

CARD_LIST_LENGTH = 10


def main():
    card_list = []
    sph_deck = SpanishDeck()
    playing_cards = list(sph_deck.playing_cards)
    for i in range(CARD_LIST_LENGTH):
        card_list.append(playing_cards.pop(choice(range(len(playing_cards)))))
    sorted_card_list = sorted(card_list, key=lambda palo: palo.trump)
    #  TODO: las cartas se ordenan por palos, pero no están ordenados por valores después

    for card in sorted_card_list:
        print(card)


if __name__ == "__main__":
    main()

"""
5. Escribe un programa que genere una secuencia de 5 cartas de la baraja española y que sume los puntos según el
juego de la brisca. El valor de las cartas se debe guardar en un diccionario que debe contener parejas (figura, valor),
por ejemplo (“caballo”, 3). La secuencia de cartas debe ser una lista que contiene objetos de la clase Carta. El valor
de las cartas es el siguiente: as → 11, tres → 10, sota → 2, caballo → 3, rey → 4; el resto de cartas no vale nada.

Author: Alberto Pérez Bernabeu
"""
from Prog.Trim2.OOP.tanda3.ej14_CardUtils import SpanishDeck
from random import choice

CARDS_TO_DEAL = 5
sph_deck = SpanishDeck()
sph_cards = list(sph_deck.playing_cards)

card_points = {'As': 11, 'Tres': 10, 'Sota': 2, 'Caballo': 3, 'Rey': 4, 'Dos': 0, 'Cuatro': 0, 'Cinco': 0,
               'Seis': 0, 'Siete': 0}


def main():
    generated_cards = []
    for i in range(CARDS_TO_DEAL):
        generated_cards.append(sph_cards.pop(choice(range(len(sph_cards)))))

    for card in generated_cards:
        print(f'{card}: {card_points[card.value]}')


if __name__ == "__main__":
    main()

import random

class Deck:

    def create_deck(self):
        suit = ['пики', 'трефы', 'червы', 'бубны']
        dignities = ['B', 'D', 'K', 'T']
        nominal = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        deck = []

        for d in dignities + nominal:
            for s in suit:
                deck.append(str(d) + ' ' + s)

        random.shuffle(deck)
        return deck
    
deck = Deck()
import random
from bot_db import game_durak

class Deck:
    def unpacking(data):
        deck = data[1].strip("]''[").split("', '")
        return deck
# Генерируем колоду и тасуем её
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
# Раздаём по 6 карт из общей колоды обновляем общую колоду
    def handing_cards(self, durak_id):
        data = game_durak.find_durak(durak_id)
        deck = data[1].strip("]''[").split("', '")
        user_deck = []
        for d in range(6):
            user_deck.append(deck[d])
        del deck[:6]
        data = dict(durak_id=data[0],
                    deck=str(deck),
                    admin_id=data[2],
                    status=data[3])
        game_durak.update_durak(data)
        return user_deck
# 
    def cards_list(self, data):
        user_deck = []
        deck = data[1].strip("]''[").split("', '")
        for d in range(6):
            user_deck.append(deck[d])
        return user_deck
    
    def unpacking(data):
        deck = data[1].strip("]''[").split("', '")
        return deck
    
deck = Deck()
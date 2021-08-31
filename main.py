import random


class Card:

    def __init__(self, suit, value):
        self.suit = suit
        self.value = value
        
    def __repr__(self):
        return ' of ' .join((self.suit, self.value))

class Deck:
    def __init__(self):
        self.cards = [Card(s, v) for s in ['Spades', 'Clubs', 'Hearts', 'Diamonds']
                      for v in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]]
    def shuffle(self):
        random.shuffle(self.cards)
    def deal(self):
        single_card = self.cards.pop()
        return single_card
class Player:
    def __init__(self, dealer=False):
        self.dealer = dealer
        self.cards = []
        self.value = 0
    def add_card(self, card):
        self.cards.append(card)
    def calculate_value(self):
        self.value = 0
        has_ace = False
        for card in self.cards:
            if card.value.isnumeric():
                self.value += int(card.value)
    def get_value(self):
        self.calculate_value
        return self.value
class Dealer(Player):
    def __init__(self):
        super().__init__()
        self.hand = []
    def display_cards(self, showall=False):
            print('Dealers hand:')
            for card in self.hand[1:]:
                print(card)
            self.calculate_value()
class Human(Player):
    def display_cards(self):
        print("\n" f'{self.name} hand after dealing card:')
        for card in self.hand:
            print(card)
            self.calculate_value()
class Game:
    def __init__(self):
        self.playing = True
    def check_for_bust(self, player):
        if player.total > 21:
            print(f'{player.name} BUST! {player.total}')
            return True
# This will Show Who Has won the game
    def compare(self, player1, player2):
        if player1.busted:
            print(f'You busted! Dealer wins! Your score is {player1.total} ; Dealer’s total is {player2.total}')
        elif player2.busted:
            print(f'You win, Dealer Busted! Your total is {player1.total}')
        elif player1.total == player2.total:
            print('It is a tie. You both had the same number!')
        elif player1.total > player2.total:
            print('You win!')
        elif player1.total < player2.total:
            print('You lose')
# main()
dealer = Dealer()
# this will eventually start our game
# game = Game()
from card import Card
import random

class Poker(object):
    #constructor
    def __init__(self):
        self._cards = [Card(suite, face) 
                       for suite in '♥♠♦♣'
                       for face in range(1, 14)]
        self._current = 0
    #getter and setter
    @property
    def cards(self):
        return self._cards
    @property
    def current(self):
        return self._current
    
    #TODO: class functions go here: 1. shuffle cards 2.give player a card on top stack.
    def shuffle(self):
        self._current = 0
        random.shuffle(self._cards)

    # @property
    def next(self):
        """give a card"""
        card = self._cards[self._current]
        self._current += 1
        return card
    
    def showPoker(self):
        for item in self._cards:
            #print(item.showCard())
            item.showCard()

  #some test code   
# def main():
#    p = Poker()
#    p.showPoker()


# if __name__ == '__main__':
#     main()
import random

class deck:
    # currentCard = 0
    cardStore = {}
    suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
    ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')

    values = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8, 'Nine': 9, 'Ten': 10,
              'Jack': 10, 'Queen': 10, 'King': 10, 'Ace': 11}

    def __init__(self):
        i = 0;
        self.currentCard = 0;
        for suit in self.suits:
            for rank in self.ranks:
                self.cardStore[i] = {suit : rank}
                i = i + 1

        random.shuffle(self.cardStore)
        pass

    def get_card_store(self):
        return self.cardStore

    def get_first_card(self):
        firstCard = self.cardStore[self.currentCard]
        self.currentCard += 1

        return firstCard
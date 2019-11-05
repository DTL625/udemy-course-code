import BJ_Mods.DeckMods as deckMods

class player:
    deckMod = deckMods.deck();
    cardValues = deckMod.values

    def __init__(self, name):
        self.name = name
        self.hand_card = {}
        self.bets = 1000
        self.currentCard = 0
        self.score = 0
        self.ace = 0

    def get_card(self, newCard):
        # cal score
        self.cal_score(newCard)
        # get card
        self.hand_card[self.currentCard] = newCard
        self.currentCard += 1

    def cal_score(self, newCard):
        # get val string
        newCardVal = next(iter(newCard.values()))
        if newCardVal == 'Ace':
            self.ace += 1

        self.score += self.cardValues[newCardVal];

        if (self.score > 21 and self.ace > 0):
            self.ace -= 1
            self.score -= 10

    def show_hand_cards(self, showAll = True):
        handCard = ''
        showScore = 0
        showHandCard = [];
        showHandCnt = 0
        for (cardNum, cardItem) in self.hand_card.items():
            for (suit, value) in cardItem.items():
                if (showAll == False):
                    if (showHandCnt > 0):
                        handCard = '[{}]*'.format(showHandCnt + 1)
                    else:
                        cardVal = next(iter(cardItem.values()))
                        showScore = self.cardValues[cardVal]
                        handCard = '[{}]{}-{}'.format(showHandCnt + 1, suit, value)
                else:
                    showScore = self.score;
                    handCard = '[{}]{}-{}'.format(showHandCnt + 1, suit, value)

                showHandCard.insert(showHandCnt, handCard);
                showHandCnt += 1
        print(f'player:{self.name} \t current score: {showScore}')
        print('hand cards: {}'.format('\t'.join(showHandCard)));
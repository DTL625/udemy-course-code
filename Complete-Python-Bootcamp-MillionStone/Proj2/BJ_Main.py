import BJ_Mods.DeckMods as deckMods
import BJ_Mods.PlayerMods as playerMods

# init
min_bet = 5
cardMod = deckMods.deck()
dealer = playerMods.player('dealer')
player = playerMods.player('player')


# 1.洗牌
cardStore = cardMod.get_card_store()
# print(f'card store: {cardStore[0]},{cardStore[1]},{cardStore[2]},{cardStore[3]}')


# 2.發牌(玩家看牌 & 莊家展示牌)
for i in range(0, 4):
    card = cardMod.get_first_card()
    if (i%2 == 1):
        dealer.get_card(card)
    else:
        player.get_card(card)
dealer.show_hand_cards(showAll = False)
player.show_hand_cards(showAll = True)
print('------------------------------')
# 3.下注
currentBet = 10
getError = True
while(getError):
    currentBet = int(input(f'請下注(每注最少${min_bet}，上限${player.bets}):'))
    if (currentBet < min_bet or currentBet > player.bets) :
        print('不合法的下注，請重新下注')
    else:
        getError = False

getMoreCard = 'y'
# 4.玩家是否要牌？（是/否）
while (getMoreCard == 'y') :
    card = cardMod.get_first_card()
    player.get_card(card)
    player.show_hand_cards()
    getMoreCard = input(f'是否還要牌？（y/n）')

# 5.莊家是否要牌？（是/否）
# 6.計算分數
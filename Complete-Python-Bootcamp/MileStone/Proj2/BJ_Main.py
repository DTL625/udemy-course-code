import os
import BJ_Mods.DeckMods as deckMods
import BJ_Mods.PlayerMods as playerMods

# init
min_bet = 5
statusMod = PlayerMods.player
dealer = PlayerMods.player('dealer')
player = PlayerMods.player('user1')

def show_result(dealShowAll = False):
    os.system('clear')
    dealer.show_hand_cards(dealShowAll)
    print('\n')
    player.show_hand_cards(showAll = True)

def check_if_get_more(moreString):
    getError = True
    while (getError):
        getMoreCard = input(moreString).lower()
        if (getMoreCard != 'y' and getMoreCard != 'n'):
            print('[輸入錯誤，請重新輸入]', end='')
        else:
            return (getMoreCard == 'y')

def show_winner(winner, loser):
    winner.bets += currentBet
    loser.bets -= currentBet
    winner.status = 'Winner!!!'


getMoreRound = True
while (getMoreRound):
    # 1.洗牌
    cardMod = DeckMods.deck()
    cardStore = cardMod.get_card_store()
    player.get_new_round()
    dealer.get_new_round()
    # print(f'card store: {cardStore[0]},{cardStore[1]},{cardStore[2]},{cardStore[3]}')

    # 2.發牌(玩家看牌 & 莊家展示牌)
    for i in range(0, 4):
        card = cardMod.get_first_card()
        if (i%2 == 1):
            dealer.get_card(card)
        else:
            player.get_card(card)
    show_result()

    # 3.下注
    currentBet = 10
    getError = True
    while(getError):
        currentBet = input(f'請下注(每注最少${min_bet}，上限${player.bets}):')
        if not currentBet:
            currentBet = 0

        currentBet = int(currentBet);
        if (currentBet < min_bet or currentBet > player.bets) :
            print('不合法的下注，請重新下注')
        else:
            getError = False

    # 4 玩家先
    getMoreCard = check_if_get_more(f'是否還要牌？（y/n）')
    while (getMoreCard == True) :
        card = cardMod.get_first_card()
        player.get_card(card)
        show_result()
        if (player.status == statusMod.STATUS_NORMAL):
            getMoreCard = check_if_get_more(f'是否還要牌？（y/n）')
        elif (player.status == statusMod.STATUS_BJ):
            getMoreCard = False
        elif (player.status == statusMod.STATUS_BUSTS):
            getMoreCard = False

    getMoreCard = (player.status != statusMod.STATUS_BUSTS and dealer.score <= 17)
    # 5.莊家是否要牌？（是/否）
    while (getMoreCard == True) :
        card = cardMod.get_first_card()
        dealer.get_card(card)
        getMoreCard = (dealer.score <= 17)

    # 6.計算分數
    if (player.status == statusMod.STATUS_BUSTS and dealer.status == statusMod.STATUS_NORMAL):
        show_winner(dealer, player)
    elif (dealer.status == statusMod.STATUS_BUSTS and player.status == statusMod.STATUS_NORMAL) :
        show_winner(player, dealer)
    else:
        if (dealer.score >= player.score):
            show_winner(dealer, player)
        else:
            show_winner(player, dealer)

    show_result(dealShowAll = True)
    getMoreRound = check_if_get_more(f'是否再來一局？（y/n）')

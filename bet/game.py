from random import randint
class Game:
    def __init__(self, players):
        pass
    #hàm tung xúc sắc ngẫu nhiên
    def randomdice(self, ):
        dice1 = randint(1,6)
        dice2 = randint(1,6)
        dice3 = randint(1,6)
        total = dice1+dice2+dice3
        threekind = (dice1 == dice2 == dice3)
        return total, threekind
    def valid_bet(self, bet, player):
        if bet < 0: 
            return False,
        if bet > player.account:
            return False,
        return True,
    def result(self, total, threekind, bet, choice):
        if choice == 'over' and total > 10 and not threekind:
            return bet*0.25
        elif choice == 'under' and total <= 10 and not threekind:
            return bet*0.25
        elif choice == 'threekind' and threekind:
            return bet*2
        else:
            return -bet

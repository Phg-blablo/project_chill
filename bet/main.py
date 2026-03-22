from player import Player
from game import Game
from ranking import Rank
#hàm khởi động trò chơi, hỏi số lượng người, hỏi tuổi
def create_players ():
    num_players = int(input('Nhập số lượng người chơi: '))
    players = []
    for i in range (num_players):
        name = input(f'Nhập tên người chơi: {i+1}: ')
        while True:
            try:
                age = int(input('Nhập số tuổi của người chơi: '))
                if age <16:
                    print('Người chơi phải trên 16 tuổi!, vui lòng nhập lai')
                    continue
                break
            except ValueError:
                print('Hãy nhập lại đúng định dạng!')
        player = Player(name, age)
        players.append(player)
        print(f'Welcome {player.name}, you have: {player.account}')
    return players
def bet_amount (player):
    while True:
        try:
            bet = float(input("Nhập số tiền cược: "))
            if bet < 0:
                print("Số tiền phải lớn hơn 0, vui lòng nhập lại!")
                continue
            if bet > player.account:
                print("Số dư không đủ, vui lòng cược lại!")
                continue
            print(f'Bạn đã cược: {bet}')
            return bet
        except ValueError:
            print("Invalid input")
def bet_choice(player, bet):
    while True:
        choice = input("Đạt cược (over/under/threekind): ").strip().lower()
        valid_choices = ["over", "under", "threekind"]
        if choice in valid_choices:
            print(f"Bạn đã đặt {choice} với số tiền {bet}")
            return choice
        print("Invalid input, try again!")

def main():
    players = create_players()
    for player in players:
        print(f'\nLượt của: {player.name}')
        bet = bet_amount(player)
        choice = bet_choice(player, bet)
    game = Game(players)
if __name__ == '__main__':
    main()

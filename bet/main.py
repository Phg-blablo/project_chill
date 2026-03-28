from player import Player
from game import Game
from ranking import Rank
from auth import AuthManager
from getpass import getpass
def create_players ():
    while True:
        try:
            num_players = int(input('Nhập số lượng người chơi: '))
            break
        except ValueError:
            print("Invalid input, vui lòng nhập lại")
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
def bet_choice( bet):
    while True:
        choice = input("Đạt cược (over/under/threekind): ").strip().lower()
        valid_choices = ["over", "under", "threekind"]
        if choice in valid_choices:
            print(f"Bạn đã đặt {choice} với số tiền {bet}")
            return choice
        print("Invalid input, try again!")
def play_turn(player, game):
    bet = bet_amount(player)
    choice = bet_choice(bet)
    dice, total, threekind = game.randomdice()
    result = game.result(total, threekind, bet, choice)
    player.account += result
    show_result(player, dice, total, result)
def show_result(player, dice, total, result):
    print(f'\n{player.name} tung: {dice}')
    print(f'Tổng: {total}')
    if result > 0:
        print(f'Bạn đã thắng: {result}')
    else:
        print(f'Bạn đã thua: {result}')
    print(f'Số dư hiện tại: {player.account}')
def show_ranking(players):
    print(f'\nFinal Ranking')
    for i, player in enumerate(players, start = 1):
        print(f'{i}. {player.name} - {player.account:.2f}')
def sign_up(auth):
    print("\nSign Up")
    while True:
        username = input("Nhap ten: ").strip()
        if auth.user_exists(username):
            print("Tên đã tồn tại, vui lòng nhập tên khác!")
            continue
        password = getpass("Nhap mat khau: ").strip()
        confirm = getpass("Nhap lai mat khau").strip()
        if password != confirm:
            print("Mật khẩu không trùng khớp, vui lòng nhập lại")
            continue
        auth.sign_up(username, password, confirm)
        print(f"Đăng kí thành công! với username: {username}")
        return
def log_in(auth):
    print("\nĐăng nhập")
    while True:
        username = input("Nhập tên đăng nhập: ").strip()
        password = getpass("Nhập mật khẩu: ").strip()
        verified = auth.log_in(username, password)
        if verified:
            print(f"Welcome to the game user: {username}")
            return True
        print("Tai khoankhong ton tai hoac sai mat khau, vui long thu lai ")
        print("[1]. Thu lai")
        print("[2]. Dang ki")
        print("[3]. Thoat")
        choice = input("Chon: ").strip()
        if choice == "1":
            continue
        elif choice == "2":
            sign_up(auth)
            continue
        elif choice == "3":
            print("Exit...")
            return False
        else:
            print("Invalid input")
            continue
def log_out(auth):
    if not auth.is_login():
        print("Chưa có tài khoản đăng nhập")
        return
    username = auth.log_out()
    print(f"Cảm ơn {username} đã sử dụng, hẹn gặp lại")
def printing_diagram():
    print(r"""
 __        _______ _     ____ ___  __  __ _____   _____ ___    _____ _   _ _____    ____    _    __  __ _____ 
 \ \      / / ____| |   / ___/ _ \|  \/  | ____| |_   _/ _ \  |_   _| | | | ____|  / ___|  / \  |  \/  | ____|
  \ \ /\ / /|  _| | |  | |  | | | | |\/| |  _|     | || | | |   | | | |_| |  _|   | |  _  / _ \ | |\/| |  _|  
   \ V  V / | |___| |__| |__| |_| | |  | | |___    | || |_| |   | | |  _  | |___  | |_| |/ ___ \| |  | | |___ 
    \_/\_/  |_____|_____\____\___/|_|  |_|_____|   |_| \___/    |_| |_| |_|_____|  \____/_/   \_\_|  |_|_____|
                                                                                                                                                                                                                                                                            
""")
def main():
   from player import Player
from game import Game
from ranking import Rank
from auth import AuthManager
from getpass import getpass
def create_players ():
    while True:
        try:
            num_players = int(input('Nhập số lượng người chơi: '))
            break
        except ValueError:
            print("Invalid input, vui lòng nhập lại")
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
def bet_choice( bet):
    while True:
        choice = input("Đạt cược (over/under/threekind): ").strip().lower()
        valid_choices = ["over", "under", "threekind"]
        if choice in valid_choices:
            print(f"Bạn đã đặt {choice} với số tiền {bet}")
            return choice
        print("Invalid input, try again!")
def play_turn(player, game):
    bet = bet_amount(player)
    choice = bet_choice(bet)
    dice, total, threekind = game.randomdice()
    result = game.result(total, threekind, bet, choice)
    player.account += result
    show_result(player, dice, total, result)
def show_result(player, dice, total, result):
    print(f'\n{player.name} tung: {dice}')
    print(f'Tổng: {total}')
    if result > 0:
        print(f'Bạn đã thắng: {result}')
    else:
        print(f'Bạn đã thua: {result}')
    print(f'Số dư hiện tại: {player.account}')
def show_ranking(players):
    print(f'\nFinal Ranking')
    for i, player in enumerate(players, start = 1):
        print(f'{i}. {player.name} - {player.account:.2f}')
def sign_up(auth):
    print("\nSign Up")
    while True:
        username = input("Nhap ten: ").strip()
        if auth.user_exists(username):
            print("Tên đã tồn tại, vui lòng nhập tên khác!")
            continue
        password = getpass("Nhap mat khau: ").strip()
        confirm = getpass("Nhap lai mat khau").strip()
        if password != confirm:
            print("Mật khẩu không trùng khớp, vui lòng nhập lại")
            continue
        auth.sign_up(username, password, confirm)
        print(f"Đăng kí thành công! với username: {username}")
        return
def log_in(auth):
    print("\nĐăng nhập")
    while True:
        username = input("Nhập tên đăng nhập: ").strip()
        password = getpass("Nhập mật khẩu: ").strip()
        verified = auth.log_in(username, password)
        if verified:
            print(f"Welcome to the game user: {username}")
            return True
        print("Tai khoankhong ton tai hoac sai mat khau, vui long thu lai ")
        print("[1]. Thu lai")
        print("[2]. Dang ki")
        print("[3]. Thoat")
        choice = input("Chon: ").strip()
        if choice == "1":
            continue
        elif choice == "2":
            sign_up(auth)
            continue
        elif choice == "3":
            print("Exit...")
            return False
        else:
            print("Invalid input")
            continue
def log_out(auth):
    if not auth.is_login():
        print("Chưa có tài khoản đăng nhập")
        return
    username = auth.log_out()
    print(f"Cảm ơn {username} đã sử dụng, hẹn gặp lại")
def printing_diagram():
    print(r"""
 __        _______ _     ____ ___  __  __ _____   _____ ___    _____ _   _ _____    ____    _    __  __ _____ 
 \ \      / / ____| |   / ___/ _ \|  \/  | ____| |_   _/ _ \  |_   _| | | | ____|  / ___|  / \  |  \/  | ____|
  \ \ /\ / /|  _| | |  | |  | | | | |\/| |  _|     | || | | |   | | | |_| |  _|   | |  _  / _ \ | |\/| |  _|  
   \ V  V / | |___| |__| |__| |_| | |  | | |___    | || |_| |   | | |  _  | |___  | |_| |/ ___ \| |  | | |___ 
    \_/\_/  |_____|_____\____\___/|_|  |_|_____|   |_| \___/    |_| |_| |_|_____|  \____/_/   \_\_|  |_|_____|
                                                                                                                                                                                                                                                                            
""")
def main():
    auth = AuthManager()
    printing_diagram()
    while True:
        if not auth.is_login():
            print("\nMenu")
            print("[1]. Đăng kí")
            print("[2]. Đăng nhập")
            print("[3]. Exit")
            choice = input("Chọn: ").strip()
            if choice == "1":
                sign_up(auth)
            elif choice == "2":
                log_in(auth)
            elif choice == "3":
                print("Bye Bye")
                break
            else:
                print("Invalid input, try again")
        else:
            print(f'\nXin chào, {auth.get_current_user()}')
            print("[1] Play")
            print("[2] Log out")
            print("[0] Exit")
            menu = input("Chọn: ").strip()
            if menu == "1":
                players = create_players()
                game = Game(players)
                while True:
                    active = [p for p in players if p.account > 0]
                    if not active:
                        print('\nTất cả người chơi đã hết tiền')
                        replay = input("Có muốn chơi lại không? (yes/no): ").strip().lower()
                        if replay == "yes":
                            players = create_players()
                            game = Game(players)
                            continue
                        else:
                            print("Quay về menu...")
                            break
                    for player in active:
                        print(f'\nLượt của: {player.name}')
                        play_turn(player, game)
                    r = Rank(players)
                    ranking = r.ranking()
                    show_ranking(ranking)
                    again = input("\nChơi tiếp vòng này không? (yes/no): ").strip().lower()
                    if again != "yes":
                        print("Quay về menu...")
                        break
            elif menu == "2":
                log_out(auth)
            elif menu == "0":
                print("Bye Bye")
                break
            else:
                print("Invalid input, try again")
if __name__ == '__main__':
    main()
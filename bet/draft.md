    #hàm nhập số tiền
    def bet_money(self, player):
        while True:
            try:
                player.bet = float(input('enter your bet: '))
                if player.bet > player.account:
                    print('Your balance is not enough')
                elif player.bet <= 0:
                    print('Invalid bet amout. Try again')
                else:
                    print('You have bet: ', player.bet)
                    break
            except ValueError:
                print('Invalid input, try again')
        return player.bet
 #hàm chọn kết quả và đặt cược
    def bet_number(self, player):
        while True:
            try:  
                player.choice = input('enter your choice:(over,under,threekind): ').strip().lower()
                if player.choice in ['over','under','threekind']:
                    print('your choice is: ',player.choice,'with: ', player.bet)
                    return player.choice
                else:
                    print('Invalid choice')
            except ValueError:
                print('Invalid input! Try again')
#hàm thông báo kết quả
    def win_rate(self, player):
        if player.choice == 'over' and player.total >10 and not player.threekind:
            print('You win:', player.bet*1.5)
            return player.bet*1.5
        elif player.choice == 'under' and player.total <= 10 and not player.threekind:
            print('You win:', player.bet*1.5)
            return player.bet*1.5
        elif player.choice == 'threekind' and player.threekind:
            print('Three kind, you win Jackpot!!', player.bet*10)
            return player.bet*10
        else:
            print('You lose all your bet, try again')
            return -player.bet
#hàm lưu kết quả
    def play(self, player):
        self.bet_money(player)
        self.bet_number(player)
        self.randomdice(player)
        result = self.win_rate(player)
        player.account += result
        print('Your balance is:', player.account)
        return player.account

while True:
        print("[1]. Đăng kí")
        print("[2]. Đăng nhập")
        print("[3]. Đăng xuất")
        print("[4]. Exit program")
        try:
           choice =  int(input("Chọn các lựa chọn sau: "))
        except ValueError:
            print("Invalid input, try again!")
            continue
        if choice == 1:
            sign_up(auth)
        elif choice == 2:
            log_in(auth)
            break
        elif choice == 3:
            log_out(auth)
        if choice == 4:
            print("Exit....")
            return
        else:
            print("Invalid input")
            return
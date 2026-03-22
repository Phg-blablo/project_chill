#khai báo người chơi
class Player:
    def __init__ (self,name,age, account = 1000):
        self.name = name
        self.age = age
        self.account = account
        self.bet = 0
        self.choice = ""
        self.result = 0 
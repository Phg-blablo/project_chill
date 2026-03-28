#hàm ranking
class Rank:
    def __init__(self, players):
        self.players = players
    def ranking(self):
        return sorted (self.players, key = lambda p: p.account, reverse = True)
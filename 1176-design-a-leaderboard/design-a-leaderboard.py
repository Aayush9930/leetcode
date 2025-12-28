class Leaderboard:

    def __init__(self):
        self.players = defaultdict(int)

    def addScore(self, playerId: int, score: int) -> None:
        self.players[playerId] += score

    def top(self, K: int) -> int:
        res = sorted(self.players.items(), key = lambda x: x[1], reverse = True)
        total = 0
        for i in range(K):
            total += res[i][1]
        return total
    def reset(self, playerId: int) -> None:
        self.players[playerId] = 0


# Your Leaderboard object will be instantiated and called as such:
# obj = Leaderboard()
# obj.addScore(playerId,score)
# param_2 = obj.top(K)
# obj.reset(playerId)
class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        players = [i for i in range(1, n+1)]
        
        index = 0
        while len(players) != 1:
            index = (index + k - 1) % n
            players.pop(index)
            n -= 1
        
        return players[0]
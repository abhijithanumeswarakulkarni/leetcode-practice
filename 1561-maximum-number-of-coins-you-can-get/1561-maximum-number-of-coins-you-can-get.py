class Solution:
    def maxCoins(self, piles: list[int]) -> int:
        piles = list(sorted(piles, reverse=True))
        total = 0
        n = len(piles)
        i, j = 0, n-1

        while i < j:
            total += piles[i+1]
            i += 2
            j -= 1
        
        return total
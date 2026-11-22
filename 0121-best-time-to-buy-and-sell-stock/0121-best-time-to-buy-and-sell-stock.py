class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        n = len(prices)
        i, j = 0, 0
        maxi = 0

        while j < n:
            while i < j and prices[i] > prices[j]:
                i += 1
            
            maxi = max(maxi, prices[j] - prices[i])
            j += 1
        
        return maxi
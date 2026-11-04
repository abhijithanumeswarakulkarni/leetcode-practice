class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        min_so_far, max_profit = float('inf'), 0
        n = len(prices)

        for i in range(n):
            min_so_far = min(min_so_far, prices[i])
            max_profit = max(max_profit, prices[i] - min_so_far)
        
        return max_profit
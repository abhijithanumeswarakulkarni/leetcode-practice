class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        n = len(prices)
        def solve(index, canBuy, dp):
            if index == n:
                return 0
            
            if dp[index][canBuy] == -1:
                opt1 = 0
                if canBuy:
                    opt1 = solve(index+1, not canBuy, dp) - prices[index]
                opt2 = 0
                if not canBuy:
                    opt2 = prices[index] + solve(index+1, not canBuy, dp) - fee
                opt3 = solve(index+1, canBuy, dp)

                dp[index][canBuy] = max(opt1, opt2, opt3)
            
            return dp[index][canBuy]
            
        dp = [[-1] * 2 for _ in range(n)]
        return solve(0, 1, dp)    
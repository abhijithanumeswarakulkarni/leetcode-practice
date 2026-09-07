class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        def solve(index, canSell, dp):
            if index == n:
                return 0
            
            if dp[index][canSell] == -1:
                opt1 = 0
                if canSell:
                    opt1 = prices[index] + solve(index+1, 0, dp)
                
                opt2 = solve(index+1, 1, dp) - prices[index]
                opt3 = solve(index+1, canSell, dp)
                dp[index][canSell] = max(opt1, opt2, opt3)
            return dp[index][canSell]
        
        dp = [[-1] * 2 for _ in range(n)]
        return solve(0, 0, dp)
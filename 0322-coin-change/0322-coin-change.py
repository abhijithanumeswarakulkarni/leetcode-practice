class Solution:
    def coinChange(self, coins: list[int], amount: int) -> int:
        n = len(coins)
        def solve(index, remaining, dp):
            if remaining == 0:
                return 0
            
            if index == n or remaining < 0:
                return float('inf')
            
            if dp[index][remaining] == -1:
                opt1 = 1 + solve(index, remaining-coins[index], dp)
                opt2 = 1 + solve(index+1, remaining-coins[index], dp)
                opt3 = solve(index+1, remaining, dp)

                dp[index][remaining] = min(opt1, opt2, opt3)

            return dp[index][remaining]

        dp = [[-1] * (amount+1) for _ in range(n)]
        res = solve(0, amount, dp)
        return res if res != float('inf') else -1
class Solution:
    def tribonacci(self, n: int) -> int:
        def solve(i, dp):
            if i == 0 or i == 1:
                return i
            
            if i == 2:
                return 1
            
            if dp[i] == -1:
                dp[i] = solve(i-1, dp) + solve(i-2, dp) + solve(i-3, dp)

            return dp[i]
        
        dp = [-1] * (n+1)
        return solve(n, dp)
class Solution:
    def climbStairs(self, n: int, costs: List[int]) -> int:
        def solve(i, dp):
            if i == n-1:
                return 0
            
            if i > n-1:
                return float('inf')
            
            if dp[i] == -1:
                opt1 = 1 + (costs[i+1] if i + 1 < n else 0) + solve(i + 1, dp)
                opt2 = 4 + (costs[i+2] if i + 2 < n else 0) + solve(i + 2, dp)
                opt3 = 9 + (costs[i+3] if i + 3 < n else 0) + solve(i + 3, dp)
                
                dp[i] = min(opt1, opt2, opt3)
            
            return dp[i]
        
        dp = [-1] * n
        return solve(-1, dp)
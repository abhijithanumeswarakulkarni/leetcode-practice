class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        n = len(s)
        k = len(t)

        def solve(i, j, dp):
            if j == k:
                return 1
            
            if i == n:
                return 0
            
            if dp[i][j] == -1:
                pick = 0
                if s[i] == t[j]:
                    pick = solve(i + 1, j + 1, dp)
                not_pick = solve(i + 1, j, dp)
            
                dp[i][j] = pick + not_pick
            
            return dp[i][j]
        
        dp = [[-1] * k for _ in range(n)]
        return solve(0, 0, dp)
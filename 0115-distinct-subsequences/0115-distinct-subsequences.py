class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        m, n = len(s), len(t)

        def solve(i, j, dp):
            if j == n:
                return 1
                
            if i == m:
                return 0
            
            if dp[i][j] == -1:
                opt1 = 0
                if s[i] == t[j]:
                    opt1 = solve(i+1, j+1, dp)
                
                opt2 = solve(i+1, j, dp)

                dp[i][j] = opt1 + opt2
            
            return dp[i][j]
        
        dp = [[-1] * n for _ in range(m)]
        return solve(0, 0, dp)
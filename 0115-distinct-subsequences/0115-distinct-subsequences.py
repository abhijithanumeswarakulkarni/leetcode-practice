class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        # m, n = len(s), len(t)

        # def solve(i, j, dp):
        #     if j == n:
        #         return 1
                
        #     if i == m:
        #         return 0
            
        #     if dp[i][j] == -1:
        #         opt1 = 0
        #         if s[i] == t[j]:
        #             opt1 = solve(i+1, j+1, dp)
                
        #         opt2 = solve(i+1, j, dp)

        #         dp[i][j] = opt1 + opt2
            
        #     return dp[i][j]
        
        # dp = [[-1] * n for _ in range(m)]
        # return solve(0, 0, dp)

        m, n = len(s), len(t)
        dp = [[-1] * (n+1) for _ in range(m+1)]
        dp[m][n] = 1
        for i in range(m):
            dp[i][n] = 1
        for j in range(n):
            dp[m][j] = 0
        
        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
                opt1 = 0
                if s[i] == t[j]:
                    opt1 = dp[i+1][j+1]
                opt2 = dp[i+1][j]
                dp[i][j] = opt1 + opt2
        
        return dp[0][0]
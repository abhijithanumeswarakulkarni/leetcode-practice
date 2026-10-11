class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        n = len(s)
        k = len(t)
        
        dp = [[0] * (k + 1) for _ in range(n+1)]
        for i in range(n+1):
            dp[i][k] = 1
        
        for i in range(n-1, -1, -1):
            for j in range(k-1, -1, -1):
                pick = 0
                if s[i] == t[j]:
                    pick = dp[i + 1][j + 1]
                not_pick = dp[i + 1][j]
                dp[i][j] = pick + not_pick
        
        return dp[0][0]
        



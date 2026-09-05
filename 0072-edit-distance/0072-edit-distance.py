class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)
        def solve(i, j, dp):
            if i == m:
                return n-j
            if j == n:
                return m-i
            
            if dp[i][j] == -1:
                if word1[i] == word2[j]:
                    dp[i][j] = solve(i+1, j+1, dp)
                else:
                    opt1 = 1 + solve(i, j+1, dp)
                    opt2 = 1 + solve(i+1, j, dp)
                    opt3 = 1 + solve(i+1, j+1, dp)
                    dp[i][j] = min(opt1, opt2, opt3)
            
            return dp[i][j]
        
        dp = [[-1] * n for _ in range(m)]
        return solve(0, 0, dp)
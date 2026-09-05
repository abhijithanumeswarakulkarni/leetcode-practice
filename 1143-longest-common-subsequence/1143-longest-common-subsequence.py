class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m, n = len(text1), len(text2)
        def solve(i, j, dp):
            if i == m or j == n:
                return 0
            if dp[i][j] == -1:
                opt1 = 0
                if text1[i] == text2[j]:
                    opt1 = 1 + solve(i+1, j+1, dp)
                opt2 = solve(i+1, j, dp)
                opt3 = solve(i, j+1, dp)

                dp[i][j] = max(opt1, opt2, opt3)
            return dp[i][j]
        
        dp = [[-1] * n for _ in range(m)]
        return solve(0, 0, dp)
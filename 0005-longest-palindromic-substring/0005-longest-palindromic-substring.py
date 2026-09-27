class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        dp = [[False] * n for _ in range(n)]
        
        # Single char is palindrome
        for i in range(n):
            dp[i][i] = True
        res = [0, 0]
        
        # Even length palindromes
        for i in range(n-1):
            if s[i] == s[i+1]:
                dp[i][i+1] = True
                res = [i, i+1]
        
        # Odd Length
        for diff in range(2, n):
            for i in range(n-diff):
                j = i + diff
                if s[i] == s[j] and dp[i+1][j-1]:
                    dp[i][j] = True
                    res = [i, j]
        
        return s[res[0]: res[1]+1]

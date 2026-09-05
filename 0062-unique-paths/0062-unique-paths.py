class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        def solve(i, j, dp):
            if i == m-1 and j == n-1:
                return 1
            if i >= m or j >= n:
                return 0
            
            if dp[i][j] == -1:
                right = solve(i, j+1, dp)
                down = solve(i+1, j, dp)
                dp[i][j] = right + down

            return dp[i][j]
        
        dp = [[-1] * n for _ in range(m)]
        return solve(0, 0, dp)
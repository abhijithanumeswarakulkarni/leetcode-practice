class Solution:
    def minPathSum(self, grid: list[list[int]]) -> int:
        m, n = len(grid), len(grid[0])
        directions = [(0, 1), (1, 0)]

        def solve(i, j, dp):
            if i == m-1 and j == n-1:
                return grid[i][j]
            
            if dp[i][j] == -1:
                mini = float('inf')
                for dire in directions:
                    updated_i, updated_j = i + dire[0], j + dire[1]
                    if updated_i < m and updated_j < n:
                        mini = min(mini, grid[i][j] + solve(updated_i, updated_j, dp))
                dp[i][j] = mini
            return dp[i][j]
        
        dp = [[-1] * n for _ in range(m)]
        return solve(0, 0, dp)
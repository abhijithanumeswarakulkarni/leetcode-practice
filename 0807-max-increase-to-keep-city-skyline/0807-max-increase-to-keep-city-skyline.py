class Solution:
    def maxIncreaseKeepingSkyline(self, grid: list[list[int]]) -> int:
        res = 0
        m, n = len(grid), len(grid[0])
        rows, cols = [-1] * m, [-1] * n
        
        for i in range(m):
            for j in range(n):
                rows[i] = max(rows[i], grid[i][j])
                cols[j] = max(cols[j], grid[i][j])
        
        for i in range(m):
            for j in range(n):
                change = min(rows[i], cols[j])
                diff = change - grid[i][j]
                res += diff
        
        return res
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        def dfs_util(i, j):
            for dire in directions:
                updated_i, updated_j = i + dire[0], j + dire[1]
                if updated_i >= 0 and updated_i < m and updated_j >= 0 and updated_j < n and grid[updated_i][updated_j] == '1':
                    grid[updated_i][updated_j] = '0'
                    dfs_util(updated_i, updated_j)
        
        count = 0

        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    dfs_util(i, j)
                    count += 1

        return count
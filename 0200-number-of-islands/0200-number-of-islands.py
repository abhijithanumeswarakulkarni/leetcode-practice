class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])
        visited = [[False] * n for _ in range(m)]
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        def dfs(i, j):
            if grid[i][j] != '1':
                return
            
            visited[i][j] = True
            for dire in directions:
                updated_i, updated_j = i + dire[0], j + dire[1]
                if updated_i >= 0 and updated_i < m and updated_j >= 0 and updated_j < n and not visited[updated_i][updated_j]:
                    dfs(updated_i, updated_j)
        
        count = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1' and not visited[i][j]:
                    dfs(i, j)
                    count += 1
        return count
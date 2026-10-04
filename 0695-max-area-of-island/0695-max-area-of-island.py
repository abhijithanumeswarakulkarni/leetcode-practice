class Solution:
    maxi = None
    def maxAreaOfIsland(self, grid: list[list[int]]) -> int:
        m, n = len(grid), len(grid[0])
        self.maxi = 0
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        def bfs_util(i, j):
            grid[i][j] = 0
            queue = [(i, j)]
            total_area = 1

            while queue:
                curr_i, curr_j = queue.pop(0)
                for dire in directions:
                    updated_i, updated_j = curr_i + dire[0], curr_j + dire[1]
                    if updated_i >= 0 and updated_i < m and updated_j >= 0 and updated_j < n and grid[updated_i][updated_j] == 1:
                        grid[updated_i][updated_j] = 0
                        total_area += 1
                        queue.append((updated_i, updated_j))
                        
            self.maxi = max(self.maxi, total_area)
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    bfs_util(i, j)
        
        return self.maxi
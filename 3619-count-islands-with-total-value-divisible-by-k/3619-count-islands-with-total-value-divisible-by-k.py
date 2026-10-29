class Solution:
    def countIslands(self, grid: List[List[int]], k: int) -> int:
        m, n = len(grid), len(grid[0])
        visited = [[False] * n for _ in range(m)]
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        def traverse(i, j):
            if grid[i][j] == 0:
                return 0

            visited[i][j] = True
            curr_sum = grid[i][j]
            for dire in directions:
                updated_i, updated_j = i + dire[0], j + dire[1]
                if updated_i >= 0 and updated_i < m and updated_j >= 0 and updated_j < n and grid[updated_i][updated_j] > 0 and not visited[updated_i][updated_j]:
                    curr_sum += traverse(updated_i, updated_j)
            
            return curr_sum
        
        count = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] > 0 and not visited[i][j]:
                    curr_sum = traverse(i, j)
                    if curr_sum % k == 0:
                        count += 1
        return count
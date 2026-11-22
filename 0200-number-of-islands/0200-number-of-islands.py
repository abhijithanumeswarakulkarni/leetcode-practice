class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])
        count = 0
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        def bfs(i, j):
            queue = deque([(i, j)])
            grid[i][j] = '-1'
            while queue:
                curr_i, curr_j = queue.popleft()
                for dire in directions:
                    updated_i, updated_j = curr_i + dire[0], curr_j + dire[1]
                    if updated_i >= 0 and updated_i < m and updated_j >= 0 and updated_j < n and grid[updated_i][updated_j] == '1':
                        queue.append((updated_i, updated_j))
                        grid[updated_i][updated_j] = '-1'


        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    bfs(i, j)
                    count += 1
        
        return count
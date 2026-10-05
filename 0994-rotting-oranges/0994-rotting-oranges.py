class Solution:
    def orangesRotting(self, grid: list[list[int]]) -> int:
        m, n = len(grid), len(grid[0])
        
        def find_rotten():
            res = []
            for i in range(m):
                for j in range(n):
                    if grid[i][j] == 2:
                        res.append((i, j, 0))
            return res
        
        def check_rotten():
            for i in range(m):
                for j in range(n):
                    if grid[i][j] == 1:
                        return False
            return True

        queue = find_rotten()
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        last_cycle = 0

        while queue:
            i, j, cycle = queue.pop(0)
            for dire in directions:
                updated_i, updated_j = i + dire[0], j + dire[1]
                if updated_i >= 0 and updated_i < m and updated_j >= 0 and updated_j < n and grid[updated_i][updated_j] == 1:
                    grid[updated_i][updated_j] = 2
                    queue.append((updated_i, updated_j, cycle + 1))
            last_cycle = cycle
        
        return last_cycle if check_rotten() else -1
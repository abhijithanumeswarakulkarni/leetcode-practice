class Solution:
    def closedIsland(self, grid: list[list[int]]) -> int:
        m, n = len(grid), len(grid[0])
        visited = [[False] * n for _ in range(m)]
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        def check_closed(curr_visited):
            for item in curr_visited:
                if item[0] == 0 or item[0] == m-1 or item[1] == 0 or item[1] == n-1:
                    return False
            return True


        def traverse(i, j, curr_visited):
            if grid[i][j] == 1:
                return

            curr_visited.append((i, j))
            visited[i][j] = True

            for dire in directions:
                updated_i, updated_j = i + dire[0], j + dire[1]
                if updated_i < m and updated_j < n and updated_i >= 0 and updated_j >= 0 and not visited[updated_i][updated_j]:
                    traverse(updated_i, updated_j, curr_visited)
            
        count = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0 and not visited[i][j]:
                    curr_visited = []
                    traverse(i, j, curr_visited)
                    if check_closed(curr_visited):
                        count += 1
        
        return count
class Solution:
    def latestDayToCross(self, row: int, col: int, cells: list[list[int]]) -> int:
        # Brute Force - TLE
        direction = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        def dfs(i, j, visited):
            if i == row-1:
                return True
            
            visited[i][j] = True
            for dire in direction:
                updated_i, updated_j = i + dire[0], j + dire[1]
                if updated_i >= 0 and updated_i < row and updated_j >= 0 and updated_j < col and not visited[updated_i][updated_j] and grid[updated_i][updated_j] != 1:
                    res = dfs(updated_i, updated_j, visited)
                    if res:
                        return True
            
            return False
        
        # res = 0
        # for index, cell in enumerate(cells):
        #     x, y = cell
        #     grid[x-1][y-1] = 1
        #     possible = False
        #     visited = [[False] * col for _ in range(row)]
        #     for start in range(col):
        #         if grid[0][start] != 1 and not visited[0][start]:
        #             can_cross = dfs(0, start, visited)
        #             if can_cross:
        #                 possible = True
        #                 break
        #     if not possible:
        #         res = index
        #         break
        n = len(cells)
        left, right = 0, n-1
        
        while left < right:
            mid = (left + right) // 2
            grid = [[0] * col for _ in range(row)]
            for x, y in cells[:mid+1]:
                grid[x-1][y-1] = 1
            possible = False
            visited = [[False] * col for _ in range(row)]
            for start in range(col):
                if grid[0][start] != 1 and not visited[0][start]:
                    can_cross = dfs(0, start, visited)
                    if can_cross:
                        possible = True
                        break
            if not possible:
                right = mid
            else:
                left = mid + 1
        return left
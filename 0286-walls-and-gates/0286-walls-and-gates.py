class Solution:
    INF = 2147483647
    def wallsAndGates(self, rooms: list[list[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        # m, n = len(rooms), len(rooms[0])
        # directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        # visited = [[False] * n for _ in range(m)]
        # ogvisited = [[False] * n for _ in range(m)]

        # def dfs_util(i, j):
        #     if rooms[i][j] == 0:
        #         return 0
            
        #     visited[i][j] = True
        #     mini = rooms[i][j]
        #     for direction in directions:
        #         updated_i, updated_j = i + direction[0], j + direction[1]
        #         if updated_i >= 0 and updated_i < m and updated_j >= 0 and updated_j < n and not visited[updated_i][updated_j] and rooms[updated_i][updated_j] != -1:
        #             mini = min(mini, 1 + dfs_util(updated_i, updated_j))
        #     visited[i][j] = False

        #     return mini
        
        # for i in range(m):
        #     for j in range(n):
        #         if rooms[i][j] == self.INF:
        #             rooms[i][j] = dfs_util(i, j)

        m, n = len(rooms), len(rooms[0])
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        def dfs_util(i, j, distance):
            rooms[i][j] = min(rooms[i][j], distance)
            
            for d in directions:
                updated_i, updated_j = i + d[0], j + d[1]
                if updated_i >= 0 and updated_i < m and updated_j >= 0 and updated_j < n and rooms[updated_i][updated_j] != -1 and rooms[updated_i][updated_j] != 0 and rooms[updated_i][updated_j] > (distance + 1):
                    dfs_util(updated_i, updated_j, distance + 1)
            
        for i in range(m):
            for j in range(n):
                if rooms[i][j] == 0:
                    dfs_util(i, j, 0)
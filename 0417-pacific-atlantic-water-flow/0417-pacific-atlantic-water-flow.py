class Solution:
    def pacificAtlantic(self, heights: list[list[int]]) -> list[list[int]]:
        m, n = len(heights), len(heights[0])
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        
        # Atlantic pass
        queue = [(m-1, j) for j in range(n)] + [(i, n-1) for i in range(m)]
        visited = [[False] * n for _ in range(m)]
        atlantic = set(queue)
        while queue:
            i, j = queue.pop()
            atlantic.add((i, j))
            visited[i][j] = True
            for dire in directions:
                updated_i, updated_j = i + dire[0], j + dire[1]
                if updated_i >= 0 and updated_i < m and updated_j >= 0 and updated_j < n and heights[updated_i][updated_j] >= heights[i][j] and not visited[updated_i][updated_j]:
                    queue.append([updated_i, updated_j])
        
        # Pacific pass
        queue = [(0, j) for j in range(n)] + [(i, 0) for i in range(m)]
        visited = [[False] * n for _ in range(m)]
        pacific = set(queue)
        while queue:
            i, j = queue.pop()
            pacific.add((i, j))
            visited[i][j] = True
            for dire in directions:
                updated_i, updated_j = i + dire[0], j + dire[1]
                if updated_i >= 0 and updated_i < m and updated_j >= 0 and updated_j < n and heights[updated_i][updated_j] >= heights[i][j] and not visited[updated_i][updated_j]:
                    queue.append([updated_i, updated_j])
        
        res = list(map(lambda x: list(x), pacific.intersection(atlantic)))
        return res
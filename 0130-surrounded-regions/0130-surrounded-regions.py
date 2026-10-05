class Solution:
    def solve(self, board: list[list[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m, n = len(board), len(board[0])
        visited = [[False] * n for _ in range(m)]
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        queue = []
        has_x, can_surround_regions = False, False
        
        for i in range(m):
            for j in range(n):
                if board[i][j] == 'X':
                    has_x = True
                if board[i][j] == 'O' and i != 0 and j != 0 and i != m-1 and j != n-1:
                    can_surround_regions = True
        if not has_x or not can_surround_regions:
            return

        for i in range(m):
            for j in range(n):
                if (i == m-1 or i == 0 or j == n-1 or j == 0) and board[i][j] == 'O':
                    queue.append([i, j])
                    visited[i][j] = True

        while queue:
            i, j = queue.pop(0)
            visited[i][j] = True
            for dire in directions:
                updated_i, updated_j = i + dire[0], j + dire[1]
                if updated_i >= 0 and updated_i < m and updated_j >= 0 and updated_j < n and board[updated_i][updated_j] == 'O' and not visited[updated_i][updated_j]:
                    queue.append([updated_i, updated_j])
        
        for i in range(m):
            for j in range(n):
                if board[i][j] == 'O' and [i, j] and not visited[i][j]:
                    board[i][j] = 'X'
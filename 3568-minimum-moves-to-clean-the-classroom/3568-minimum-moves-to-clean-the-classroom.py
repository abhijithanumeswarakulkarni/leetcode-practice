from typing import List
from collections import deque

class Solution:
    def minMoves(self, classroom: List[str], energy: int) -> int:
        m, n = len(classroom), len(classroom[0])
        grid = classroom

        start = None
        bit_at = [[-1] * n for _ in range(m)]   # -1 = not a litter cell
        num_litter = 0
        for i in range(m):
            for j in range(n):
                c = grid[i][j]
                if c == 'S':
                    start = (i, j)
                elif c == 'L':
                    bit_at[i][j] = num_litter
                    num_litter += 1

        if num_litter == 0:
            return 0

        num_masks = 1 << num_litter
        full_mask = num_masks - 1
        num_energy = energy + 1
        directions = ((0, 1), (0, -1), (1, 0), (-1, 0))

        # Flat visited array: visited[idx(i, j, e, mask)]
        def idx(i, j, e, mask):
            return ((i * n + j) * num_energy + e) * num_masks + mask

        visited = bytearray(m * n * num_energy * num_masks)

        si, sj = start
        visited[idx(si, sj, energy, full_mask)] = 1
        queue = deque([(si, sj, energy, full_mask)])

        moves = 0
        while queue:
            for _ in range(len(queue)):          # one full BFS level = one move
                i, j, e, mask = queue.popleft()

                if mask == 0:
                    return moves
                if e == 0:
                    continue                       # stuck, no outgoing moves

                for di, dj in directions:
                    ni, nj = i + di, j + dj
                    if not (0 <= ni < m and 0 <= nj < n):
                        continue
                    cell = grid[ni][nj]
                    if cell == 'X':
                        continue

                    new_e = energy if cell == 'R' else e - 1

                    bit = bit_at[ni][nj]
                    new_mask = (mask & ~(1 << bit)) if bit >= 0 else mask

                    key = idx(ni, nj, new_e, new_mask)
                    if not visited[key]:
                        visited[key] = 1
                        queue.append((ni, nj, new_e, new_mask))

            moves += 1

        return -1
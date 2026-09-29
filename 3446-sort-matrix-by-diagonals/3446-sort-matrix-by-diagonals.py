class Solution:
    def sortMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        for k in range(n-1, 0, -1):
            diognal = []
            i, j = 0, k
            while i < m and j < n:
                diognal.append(grid[i][j])
                i += 1
                j += 1
            diognal = list(sorted(diognal))
            i, j = 0, k
            while i < m and j < n:
                grid[i][j] = diognal[i]
                i += 1
                j += 1

        for k in range(0, m):
            diognal = []
            i, j = k, 0
            while i < m and j < n:
                diognal.append(grid[i][j])
                i += 1
                j += 1
            diognal = list(sorted(diognal, reverse = True))
            i, j = k, 0
            while i < m and j < n:
                grid[i][j] = diognal[j]
                i += 1
                j += 1
        
        return grid
        
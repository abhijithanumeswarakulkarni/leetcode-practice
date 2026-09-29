class Solution:
    def diagonalSort(self, mat: list[list[int]]) -> list[list[int]]:
        m, n = len(mat), len(mat[0])

        for k in range(n-1, -1, -1):
            i, j = 0, k
            diognal = []
            while i < m and j < n:
                diognal.append(mat[i][j])
                i += 1
                j += 1
            diognal.sort()
            i, j = 0, k
            while i < m and j < n:
                mat[i][j] = diognal[i]
                i += 1
                j += 1
        
        for k in range(1, m):
            i, j = k, 0
            diognal = []
            while i < m and j < n:
                diognal.append(mat[i][j])
                i += 1
                j += 1
            diognal.sort()
            i, j = k, 0
            while i < m and j < n:
                mat[i][j] = diognal[j]
                i += 1
                j += 1
        
        return mat
class Solution:
    def restoreMatrix(self, rowSum: list[int], colSum: list[int]) -> list[list[int]]:
        m = len(rowSum)
        n = len(colSum)
        grid = [[-1] * n for _ in range(m)]
        
        for i in range(m):
            for j in range(n):
                if rowSum[i] < colSum[j]:
                    grid[i][j] = rowSum[i]
                else:
                    grid[i][j] = colSum[j]
                rowSum[i] -= grid[i][j]
                colSum[j] -= grid[i][j]
        
        return grid
                    
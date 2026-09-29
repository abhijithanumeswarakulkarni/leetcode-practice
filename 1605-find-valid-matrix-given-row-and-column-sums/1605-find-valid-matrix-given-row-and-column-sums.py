class Solution:
    def restoreMatrix(self, rowSum: list[int], colSum: list[int]) -> list[list[int]]:
        m = len(rowSum)
        n = len(colSum)
        grid = [[-1] * n for _ in range(m)]
        
        for i in range(m):
            for j in range(n):
                grid[i][j] = min(rowSum[i], colSum[j])
                rowSum[i] -= grid[i][j]
                colSum[j] -= grid[i][j]
        
        return grid
                    
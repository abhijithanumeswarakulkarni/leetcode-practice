class Solution:
    def findDegrees(self, matrix: list[list[int]]) -> list[int]:
        n = len(matrix)
        degree = {i: 0 for i in range(n)}

        for i in range(n):
            for j in range(n):
                if matrix[i][j] == 1:
                    degree[i] += 1
        
        return list(degree.values())
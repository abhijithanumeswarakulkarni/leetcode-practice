class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        frq = {}
        n = len(grid)
        repeated, missing = None, None
        
        for i in range(n):
            for j in range(n):
                if grid[i][j] not in frq:
                    frq[grid[i][j]] = 1
                else:
                    repeated = grid[i][j]
        
        for x in range(1, n ** 2 + 1):
            if x not in frq:
                missing = x
                break
        
        return [repeated, missing]
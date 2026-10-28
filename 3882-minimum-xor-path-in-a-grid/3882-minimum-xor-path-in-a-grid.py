class Solution:
    def minCost(self, grid: list[list[int]]) -> int:
        m, n = len(grid), len(grid[0])
        directions = [(0, 1), (1, 0)]
        mini = float('inf')
        
        def solve(i, j, curr_xor, dp):
            nonlocal mini

            if i == (m-1) and j == (n-1):
                mini = min(mini, curr_xor ^ grid[i][j])
                return mini
            
            if dp[i][j][curr_xor] == -1:
                for dire in directions:
                    updated_i, updated_j = i + dire[0], j + dire[1]
                    if updated_i < m and updated_j < n:
                        dp[i][j][curr_xor] = solve(updated_i, updated_j, curr_xor ^ grid[i][j], dp)
            
            return dp[i][j][curr_xor]
            

        dp = [[[-1] * (1024) for _ in range(n)] for _ in range(m)]
        solve(0, 0, 0, dp)
        return mini
class Solution:
    def hasValidPath(self, grid: list[list[str]]) -> bool:
        directions = [(0, 1), (1, 0)]
        m, n = len(grid), len(grid[0])

        def solve(i, j, open_par, dp):
            if i == m-1 and j == n-1:
                if grid[i][j] == ')' and open_par == 1:
                    return True
                return False
            
            if i >= m or j >= n:
                return False
            
            if dp[i][j][open_par] == -1:
                if grid[i][j] == '(':
                    updated_par = open_par + 1
                else:
                    if open_par <= 0:
                        return False
                    updated_par = open_par - 1

                res = False
                for dire in directions:
                    res = solve(i + dire[0], j + dire[1], updated_par, dp)
                    if res:
                        break
                
                dp[i][j][open_par] = res

            return dp[i][j][open_par]
        
        dp = [[[-1] * (m + n) for _ in range(n)] for _ in range(m)]
        return solve(0, 0, 0, dp)
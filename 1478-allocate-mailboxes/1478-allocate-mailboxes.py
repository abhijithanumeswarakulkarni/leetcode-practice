class Solution:
    def minDistance(self, houses: list[int], k: int) -> int:
        houses.sort()
        n = len(houses)

        def solve(index, curr_k, dp):
            if index >= n:
                return 0
            
            if curr_k == 0:
                return float('inf')
            
            if dp[index][curr_k] == -1:
                mini = float('inf')
                for j in range(index, n - curr_k + 1):
                    total = 0
                    mid = (index + j) // 2
                    for i in range(index, j+1):
                        total += abs(houses[i] - houses[mid])
                    res = total + solve(j + 1, curr_k - 1, dp)
                    mini = min(mini, res)
                
                dp[index][curr_k] = mini
            
            return dp[index][curr_k]
        
        dp = [[-1] * (k + 1) for _ in range(n)]
        return solve(0, k, dp)
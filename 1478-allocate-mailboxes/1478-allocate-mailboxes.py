class Solution:
    def minDistance(self, houses: list[int], k: int) -> int:
        houses.sort()
        n = len(houses)

        # def solve(index, curr_k, dp):
        #     if index >= n:
        #         return 0
            
        #     if curr_k == 0:
        #         return float('inf')
            
        #     if dp[index][curr_k] == -1:
        #         mini = float('inf')
        #         for j in range(index, n - curr_k + 1):
        #             total = 0
        #             mid = (index + j) // 2
        #             for i in range(index, j+1):
        #                 total += abs(houses[i] - houses[mid])
        #             res = total + solve(j + 1, curr_k - 1, dp)
        #             mini = min(mini, res)
                
        #         dp[index][curr_k] = mini
            
        #     return dp[index][curr_k]
        
        # dp = [[-1] * (k + 1) for _ in range(n)]
        # return solve(0, k, dp)

        dp = [[0] * (k + 1) for _ in range(n + 1)]
        for index in range(n):
            dp[index][0] = float('inf')
        
        for index in range(n-1, -1, -1):
            for curr_k in range(k, 0, -1):
                mini = float('inf')
                for j in range(index, n - curr_k + 1):
                    total = 0
                    mid = (index + j) // 2
                    print(index, j+1)
                    for i in range(index, j+1):
                        total += abs(houses[i] - houses[mid])
                    res = total + dp[j + 1][curr_k - 1]
                    mini = min(mini, res)
                
                dp[index][curr_k] = mini
        
        return dp[0][k]
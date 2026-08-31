class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        # # Greedy - Won't work
        # cost = min(costs[0])
        # prev = costs[0].index(cost)
        # idx = 1
        # n = len(costs)
        # for idx in range(1, n):
        #     minCost = min(costs[idx][:prev] + costs[idx][prev+1:])
        #     cost += minCost
        #     prev = costs[idx].index(minCost)
        
        # return cost

        # # Recursion - TLE obv
        # n = len(costs)
        # def solve(index, prev):
        #     if index == n:
        #         return 0
            
        #     mini = float('inf')
        #     for paint in range(3):
        #         if prev == -1 or paint != prev:
        #             mini = min(mini, costs[index][paint] + solve(index+1, paint))
            
        #     return mini

        # return solve(0, -1)

        # Recursion + DP
        n = len(costs)
        def solve(index, prev, dp):
            if index == n:
                return 0
            
            if dp[index][prev] == -1:
                mini = float('inf')
                for paint in range(3):
                    if prev == -1 or paint != prev:
                        mini = min(mini, costs[index][paint] + solve(index+1, paint, dp))
                
                dp[index][prev] = mini
            return dp[index][prev]

        dp = [[-1] * 3 for _ in range(n)]
        return solve(0, -1, dp)
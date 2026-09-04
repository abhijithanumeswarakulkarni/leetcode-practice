class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        def solve(index, dp):
            if index >= n:
                return 0
            
            if dp[index] == -1:
                opt1 = cost[index] + solve(index+1, dp)
                opt2 = cost[index] + solve(index+2, dp)

                dp[index] = min(opt1, opt2)
            
            return dp[index]
        
        dp = [-1] * (n+2)
        startZero = solve(0, dp)
        startOne = solve(1, dp)
        
        return min(startZero, startOne)
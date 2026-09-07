class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)

        def solve(index, dp):
            if index == n-1:
                return 0
            if index > n-1:
                return float('inf')
            
            if dp[index] == -1:
                mini = float('inf')
                for steps in range(1, nums[index]+1):
                    res = 1 + solve(index+steps, dp)
                    mini = min(mini, res)
                
                dp[index] = mini
            return dp[index]
        
        dp = [-1] * n
        return solve(0, dp)
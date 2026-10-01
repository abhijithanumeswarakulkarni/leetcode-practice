class Solution:
    def jump(self, nums: list[int]) -> int:
        # n = len(nums)

        # def solve(index, dp):
        #     if index >= n-1:
        #         return 0
            
        #     if nums[index] == 0:
        #         return float('inf')
            
        #     if dp[index] == -1:
        #         res = float('inf')
        #         for step in range(1, nums[index] + 1):
        #             res = min(res, 1 + solve(index + step, dp))
            
        #         dp[index] = res
            
        #     return dp[index]
        
        # dp = [-1] * n
        # return solve(0, dp)

        n = len(nums)
        dp = [-1] * n
        dp[n-1] = 0
        
        for index in range(n-2, -1, -1):
            res = float('inf')
            for step in range(1, nums[index] + 1):
                if index + step <= n-1:
                    res = min(res, 1 + dp[index + step])
            dp[index] = res
        
        return dp[0]
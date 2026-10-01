class Solution:
    def jump(self, nums: list[int]) -> int:
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
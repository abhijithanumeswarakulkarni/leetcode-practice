class Solution:
    def canJump(self, nums: list[int]) -> bool:
        # n = len(nums)

        # def solve(index, dp):
        #     if index >= n-1:
        #         return True
            
        #     if dp[index] == -1:
        #         dp[index] = False
        #         for step in range(1, nums[index]+1):
        #             res = solve(index + step, dp)
        #             if res:
        #                 dp[index] = True
        #                 break

        #     return dp[index]
        
        # dp = [-1] * (n)
        # return solve(0, dp)

        n = len(nums)
        dp = [False] * n
        dp[n-1] = True

        for index in range(n-2, -1, -1):
            for step in range(1, nums[index] + 1):
                res = dp[index + step]
                if res:
                    dp[index] = True
                    break
        
        return dp[0]
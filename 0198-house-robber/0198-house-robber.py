class Solution:
    def rob(self, nums: List[int]) -> int:
        # n = len(nums)
        # def solve(index, canRob, dp):
        #     if index == n:
        #         return 0
            
        #     if dp[index][canRob] == -1:
        #         opt1, opt2 = 0, 0
        #         if canRob:
        #             opt1 = nums[index] + solve(index + 1, 0, dp)
        #         else:
        #             opt2 = solve(index + 1, 1, dp)
        #         opt3 = solve(index + 1, canRob, dp)

        #         dp[index][canRob] = max(opt1, opt2, opt3)
            
        #     return dp[index][canRob]
        
        # dp = [[-1] * 2 for _ in range(n+1)]
        # return solve(0, 1, dp)

        n = len(nums)
        dp = [[-1] * 2 for _ in range(n+1)]
        dp[n] = [0, 0]

        for index in range(n-1, -1, -1):
            for canRob in range(0, 2):
                opt1, opt2 = 0, 0
                if canRob:
                    opt1 = nums[index] + dp[index + 1][0]
                else:
                    opt2 = dp[index + 1][1]
                opt3 = dp[index + 1][canRob]

                dp[index][canRob] = max(opt1, opt2, opt3)
        
        return dp[0][1]
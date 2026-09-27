class Solution:
    def rob(self, nums: list[int]) -> int:
        n = len(nums)

        def solve(index, first_robbed, dp):
            if index == n-1:
                return 0 if first_robbed else nums[index]
            
            if index >= n:
                return 0
            
            if dp[index][first_robbed] == -1:
                opt1 = 0
                if index == 0:
                    opt1 = nums[index] + solve(index+2, 1, dp)
                else:
                    opt1 = nums[index] + solve(index+2, first_robbed, dp)
                opt2 = solve(index+1, first_robbed, dp)
                
                dp[index][first_robbed] = max(opt1, opt2)
            return dp[index][first_robbed]

        dp = [[-1] * 2 for _ in range(n+2)]
        return solve(0, 0, dp)
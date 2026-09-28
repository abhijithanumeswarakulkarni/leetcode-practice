class Solution:
    def lengthOfLIS(self, nums: list[int]) -> int:
        n = len(nums)

        def solve(index, prev, dp):
            if index == n:
                return 0
            
            if dp[index][prev] == -1:
                opt1 = 0
                if prev == -1 or nums[index] > nums[prev]:
                    opt1 = 1 + solve(index+1, index, dp)
                opt2 = solve(index+1, prev, dp)

                dp[index][prev] = max(opt1, opt2)
            
            return dp[index][prev]
        
        dp = [[-1] * n for _ in range(n)]
        return solve(0, -1, dp)


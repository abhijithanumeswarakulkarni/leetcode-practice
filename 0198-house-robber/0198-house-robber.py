class Solution:
    def rob(self, nums: list[int]) -> int:
        n = len(nums)

        def solve(index, can_rob, dp):
            if index == n:
                return 0
            
            if dp[index][can_rob] == -1:
                opt1 = 0
                if can_rob:
                    opt1 = nums[index] + solve(index+1, not can_rob, dp)
                else:
                    opt1 = solve(index+1, not can_rob, dp)
                
                opt2 = solve(index+1, can_rob, dp)

                dp[index][can_rob] = max(opt1, opt2)
            
            return dp[index][can_rob]
        
        dp = [[-1] * 2 for _ in range(n)]
        return solve(0, 1, dp)
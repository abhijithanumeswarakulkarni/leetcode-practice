class Solution:
    def canPartition(self, nums: list[int]) -> bool:
        n = len(nums)
        total = sum(nums)
        if total % 2 != 0:
            return False
        half = total // 2

        def solve(index, target, dp):
            if target == 0:
                return True

            if index == n:
                return False
            
            if dp[index][target] == -1:
                opt1 = solve(index+1, target - nums[index], dp)
                opt2 = solve(index+1, target, dp)

                dp[index][target] = opt1 or opt2
            
            return dp[index][target]
        
        dp = [[-1] * (half+1) for _ in range(n)]
        return solve(0, half, dp)
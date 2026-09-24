class Solution:
    def minOperations(self, nums: list[int], x: int) -> int:
        # def solve(i, j, val, dp):
        #     if val == 0:
        #         return 0
                
        #     if i > j or val < 0:
        #         return float('inf')

        #     if (i, j, val) not in dp:
        #         opt1 = 1 + solve(i+1, j, val - nums[i], dp)
        #         opt2 = 1 + solve(i, j-1, val - nums[j], dp)
                
        #         dp[(i, j, val)] = min(opt1, opt2)
            
        #     return dp[(i, j, val)]
        
        # n = len(nums)
        # dp = {}
        # res = solve(0, n-1, x, dp)
        # return res if res != float('inf') else -1

        # Sliding window
        n = len(nums)
        total = sum(nums)
        target = total - x
        
        i, j = 0, 0
        curr_sum = 0
        max_len = float('-inf')

        while j < n:
            curr_sum += nums[j]

            while i <= j and curr_sum > target:
                curr_sum -= nums[i]
                i += 1

            if curr_sum == target:
                max_len = max(max_len, (j-i+1))

            j += 1

        return (n - max_len) if max_len != float('-inf') else -1
class Solution:
    def minOperations(self, nums: list[int], x: int) -> int:
        # MLE - DP
        # n = len(nums)

        # def solve(i, j, target, dp):
        #     if target == 0:
        #         return 0
                
        #     if i > j or target < 0:
        #         return float('inf')
            
        #     if (i, j, target) not in dp:
        #         first = 1 + solve(i + 1, j, target - nums[i], dp)
        #         last = 1 + solve(i, j - 1, target - nums[j], dp)

        #         dp[(i, j, target)] = min(first, last)
            
        #     return dp[(i, j, target)]
        
        # dp = {}
        # res = solve(0, n-1, x, dp)

        # return res if res != float('inf') else -1

        # Sliding window - Find longest subarray with sum = total - x
        n = len(nums)
        total = sum(nums)
        
        # Edge case
        if total == x:
            return n

        target = total - x
        left, right = 0, 0
        curr_sum = 0
        max_window = 0
        i, j = -1, -1

        while right < n:
            curr_sum += nums[right]

            while left < right and curr_sum > target:
                curr_sum -= nums[left]
                left += 1
            
            if curr_sum == target and (right - left + 1) > max_window:
                max_window = (right - left + 1)
                i, j = left, right
            
            right += 1
        
        return i + (n - j - 1) if i >= 0 and j >= 0 else -1

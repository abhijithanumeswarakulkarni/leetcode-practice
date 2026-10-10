class Solution:
    def numSubarrayProductLessThanK(self, nums: list[int], k: int) -> int:
        n = len(nums)
        left, right = 0, 0
        curr_prod = 1
        count = 0

        while right < n:
            curr_prod *= nums[right]

            while left < right and curr_prod > k:
                curr_prod //= nums[left]
                left += 1
            if curr_prod < k:
                count += (right - left + 1)
            right += 1
        
        return count
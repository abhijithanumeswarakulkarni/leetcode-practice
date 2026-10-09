class Solution:
    def numSubarrayProductLessThanK(self, nums: list[int], k: int) -> int:
        if k <= 1:
            return 0

        n = len(nums)
        count = 0
        left, right = 0, 0
        curr_prod = 1

        while right < n:
            curr_prod *= nums[right]

            while curr_prod >= k:
                curr_prod = curr_prod // nums[left]
                left += 1
            
            count += (right - left + 1)
            right += 1

        
        return count
class Solution:
    def reverseSubarrays(self, nums: list[int], k: int) -> list[int]:
        n = len(nums)
        t = n // k
        index = 0

        while index <= n-t:
            i, j = index, index+t-1
            while i < j:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
                j -= 1
            index += t
        
        return nums
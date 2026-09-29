class Solution:
    def reverseSubarrays(self, nums: list[int], k: int) -> list[int]:
        res = []
        n = len(nums)
        t = n // k
        index = 0

        while index < n:
            res += nums[index: index+t][::-1]
            index += t
        
        return res
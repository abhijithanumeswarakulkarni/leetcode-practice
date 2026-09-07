class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        frq = {}
        for num in nums:
            if num in frq:
                frq[num] += 1
            else:
                frq[num] = 1
        n = len(nums)
        for key, value in frq.items():
            if value > n // 2:
                return key
        return -1 # Should never reach according to constraints
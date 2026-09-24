class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        n = len(nums)
        for i in range(n):
            digits = list(map(lambda x: int(x), list(str(nums[i]))))
            if sum(digits) == i:
                return i
        
        return -1
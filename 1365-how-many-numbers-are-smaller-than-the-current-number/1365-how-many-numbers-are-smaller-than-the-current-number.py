class Solution:
    def smallerNumbersThanCurrent(self, nums: list[int]) -> list[int]:
        count = {}
        sorted_nums = list(sorted(nums, reverse=True))
        n = len(nums)

        for index, num in enumerate(sorted_nums):
            count[num] = n - index - 1
        
        res = []
        for num in nums:
            res.append(count[num])
        return res
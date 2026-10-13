class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        abs_nums = []
        for num in nums:
            abs_nums.append(abs(num))
        
        abs_nums.sort()
        n = len(abs_nums)
        i, j = 0, n-1
        total = 0

        while i < j:
            total += abs_nums[j] ** 2 - abs_nums[i] ** 2
            j -= 1
            i += 1
        
        if i == j:
            total += abs_nums[i] ** 2
        
        return total
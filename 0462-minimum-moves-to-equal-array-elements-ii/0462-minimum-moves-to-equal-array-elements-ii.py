class Solution:
    def minMoves2(self, nums: list[int]) -> int:
        n = len(nums)
        nums.sort()
        mid = n // 2
        median = None
        if n % 2 == 0:
            median = (nums[mid] + nums[mid-1]) // 2
        else:
            median = nums[mid]
        
        count = 0
        for num in nums:
            count += abs(num - median)
        
        return count
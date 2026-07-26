class Solution:
    def isConsecutive(self, nums: List[int]) -> bool:
        # Sorting - Time = O(n*log(n)), space = O(1)
        nums.sort()
        n = len(nums)
        for index in range(1, n):
            if nums[index] - nums[index-1] != 1:
                return False
        return True
class Solution:
    def minimumSwaps(self, nums: list[int]) -> int:
        zero_count = nums.count(0)
        n = len(nums)
        return nums[:n - zero_count].count(0)
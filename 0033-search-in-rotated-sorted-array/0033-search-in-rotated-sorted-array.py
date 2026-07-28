class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # Brute Force - Time = O(n), space = O(1)
        for index, num in enumerate(nums):
            if num == target:
                return index
        return -1
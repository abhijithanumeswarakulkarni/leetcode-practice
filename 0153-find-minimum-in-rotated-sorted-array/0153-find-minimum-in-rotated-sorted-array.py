class Solution:
    def findMin(self, nums: List[int]) -> int:
        # Brute force - Time = O(n), space = O(1)
        mini = float('inf')
        for num in nums:
            mini = min(mini, num)
        return mini
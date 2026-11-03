class Solution:
    def minMoves(self, nums: List[int]) -> int:
        max_ele = max(nums)
        count = 0

        for num in nums:
            count += max_ele - num
        
        return count
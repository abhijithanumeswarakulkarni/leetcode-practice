class Solution:
    def sumOfSquares(self, nums: List[int]) -> int:
        res = 0
        n = len(nums)

        for idx, num in enumerate(nums):
            if n % (idx + 1) == 0:
                res += num ** 2
        
        return res
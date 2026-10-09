class Solution:
    def concatWithReverse(self, nums: list[int]) -> list[int]:
        res = []

        for x in nums:
            res.append(x)
        
        for x in nums[::-1]:
            res.append(x)
        
        return res
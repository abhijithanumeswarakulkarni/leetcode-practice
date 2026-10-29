class Solution:
    def targetIndices(self, nums: list[int], target: int) -> list[int]:
        nums.sort()
        res = []
        
        for idx, num in enumerate(nums):
            if num == target:
                res.append(idx)
            if num > target:
                break
        
        return res
class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        num_idx = {}

        for idx, num in enumerate(nums):
            num_idx[num] = idx
        
        for idx, num in enumerate(nums):
            compliment = target - num
            if compliment in num_idx and idx != num_idx[compliment]:
                return [idx, num_idx[compliment]]
        
        return [-1, -1] # Should never reach
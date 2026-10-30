class Solution:
    def sumIndicesWithKSetBits(self, nums: List[int], k: int) -> int:
        res = 0
        
        for index, num in enumerate(nums):
            num_set_bits = bin(index)[2:].count('1')
            if num_set_bits == k:
                res += num
        
        return res
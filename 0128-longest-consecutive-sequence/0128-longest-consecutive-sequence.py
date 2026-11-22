class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        all_set = set(nums)
        res = 0

        for num in all_set:
            if num - 1 in all_set:
                continue
            
            count = 0
            while num in all_set:
                count += 1
                num += 1
            res = max(res, count)
        
        return res
class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        # Time = O(n)
        nums_set = set(nums)
        longest = 0

        for num in nums_set:
            if num - 1 in nums_set:
                continue
            
            count = 0
            while num in nums_set:
                num += 1
                count += 1
            longest = max(longest, count)
        
        return longest


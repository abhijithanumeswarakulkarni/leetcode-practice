class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        # Time = O(n)
        nums_set = set(nums)
        longest = 0
        visited = set()

        for num in nums_set:
            if num - 1 in nums_set or num in visited:
                continue
            
            count = 0
            while num in nums_set:
                visited.add(num)
                num += 1
                count += 1
            longest = max(longest, count)
        
        return longest


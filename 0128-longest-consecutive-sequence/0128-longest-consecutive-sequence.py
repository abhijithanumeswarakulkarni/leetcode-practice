class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # Brute force (sorting)
        nums = list(sorted(set(nums)))
        n = len(nums)
        
        # Edge case
        if n == 0:
            return 0
        
        maxi = float('-inf')
        i = 0
        j = 1
        while j < n:
            if nums[j] - 1 == nums[j-1]:
                j += 1
            else:
                maxi = max(maxi, (j-i))
                i = j
                j += 1
        maxi = max(maxi, (j-i))
        return maxi

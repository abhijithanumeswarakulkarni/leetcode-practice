class Solution:
    def findMaxConsecutiveOnes(self, nums: list[int]) -> int:
        i, j = 0, 0
        n = len(nums)
        maxi = 0

        while j < n:
            if nums[j] == 0:
                maxi = max(maxi, (j - i))
                i = j + 1
            j += 1
        if nums[-1] == 1:
            maxi = max(maxi, (j - i))
        
        return maxi
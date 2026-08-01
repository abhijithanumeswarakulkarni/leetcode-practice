class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        # Brute force
        n = len(nums)
        if n == 1:
            return n if nums[0] == 1 else 0
        
        i, j = 0, 1
        res = 0
        while j < n:
            if nums[i] != 1:
                while i < n and nums[i] != 1:
                    i += 1
                j = i+1
            else:
                if nums[j] != 1:
                    res = max(res, (j-i))
                    i = j+1
                    j += 2
                else:
                    j += 1
        
        if nums[-1] == 1:
            res = max(res, (j-i))
        return res
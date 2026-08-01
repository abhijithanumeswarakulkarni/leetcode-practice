class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        k = 1
        n = len(nums)
        if n == 1:
            return n
        
        l, r = 0, 0
        count = 0
        res = 0
        while r < n:
            if nums[r] == 0:
                if count == k:
                    while nums[l] != 0:
                        l += 1
                    l += 1
                else:
                    count += 1
            res = max(res, (r-l+1))
            r += 1
        return res

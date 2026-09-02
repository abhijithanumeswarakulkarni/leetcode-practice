class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        k = 1
        maxArr = 1
        l, r = 0, 0
        n = len(nums)

        while r < n:
            while k < 0:
                if nums[l] == 0:
                    k += 1
                l += 1
            
            if nums[r] == 0:
                k -= 1
            if k >= 0:
                maxArr = max(maxArr, (r-l+1))
            
            r += 1
        
        return maxArr - 1
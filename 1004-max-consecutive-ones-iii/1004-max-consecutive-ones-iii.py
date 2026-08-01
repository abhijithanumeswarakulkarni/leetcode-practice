class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        # Sliding window
        # Hint: rather than consecutive 1, look at how many zeros u can have
        n = len(nums)
        
        l, r, zeros, res= 0, 0, 0, 0
        while r < n:
            if nums[r] == 0:
                zeros += 1
            if zeros > k:
                if nums[l] == 0:
                    zeros -= 1
                l+=1
            if zeros <= k:
                res = max(res, (r-l+1))
            r += 1
        return res
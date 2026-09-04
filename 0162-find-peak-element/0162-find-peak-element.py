class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        # Brute force
        n = len(nums)
        if n == 1:
            return 0
        
        for i in range(n):
            if (i == 0 and nums[i] > nums[i+1]) or (i == n-1 and nums[i] > nums[i-1]):
                return i
            
            if nums[i] > nums[i-1] and nums[i] > nums[i+1]:
                return i
        
        return -1
class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        # Brute force - Time = O(nlog(n)), space = O(1)
        nums.sort()
        res = []
        n = len(nums)
        for index in range(n-1):
            if nums[index+1] - nums[index] > 1:
                res += range(nums[index]+1, nums[index+1])
        
        return res
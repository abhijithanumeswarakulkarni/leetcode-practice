class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # Two pointers
        n = len(nums)
        
        i, j = 0, 1
        while j < n:
            while j < n and nums[i] == nums[j]:
                j += 1
            if j < n:
                i += 1
                temp = nums[i]
                nums[i] = nums[j]
                nums[j] = temp
                j += 1
        
        return i+1
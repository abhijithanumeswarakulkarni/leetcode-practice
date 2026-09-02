class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        n = len(nums)
        # if n <= 1:
        #     return nums
        
        i, j = 0, 0
        while j < n:
            if nums[j] != 0:
                nums[i] = nums[j]
                i += 1
            j += 1
        
        while i < n:
            nums[i] = 0
            i += 1
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        i, j = n-2, n-1
        while i >= 0:
            if nums[j] > nums[i]:
                for idx in range(n-1, j-1, -1):
                    if nums[idx] > nums[i]:
                        nums[i], nums[idx] = nums[idx], nums[i]
                        break
                break
            i -= 1
            j -= 1
        
        
        k = n-1
        while j < k:
            nums[j], nums[k] = nums[k], nums[j]
            j += 1
            k -= 1
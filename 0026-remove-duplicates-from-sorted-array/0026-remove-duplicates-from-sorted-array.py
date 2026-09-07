class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)
        i, j = 0, 1
        while j < n:
            while j < n and nums[i] == nums[j]:
                j += 1
            if j == n:
                break
            nums[i+1], nums[j] = nums[j], nums[i+1]
            i += 1
            j += 1
        return (i+1)
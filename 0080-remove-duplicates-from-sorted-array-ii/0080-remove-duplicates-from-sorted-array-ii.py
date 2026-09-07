class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)
        i, j = 0, 1
        while j < n:
            count = 1
            while j < n and nums[i] == nums[j]:
                j += 1
                count += 1
            if count >= 2:
                nums[i+1] = nums[i]
                if j < n:
                    i += 2
                else:
                    i += 1
            else:
                i += 1
            if j < n:
                nums[i], nums[j] = nums[j], nums[i]
                j += 1
        return (i+1)
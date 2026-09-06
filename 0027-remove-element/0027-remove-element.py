class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i = 0
        n = len(nums)
        while i < n:
            if nums[i] == val:
                j = i + 1
                while j < n and nums[j] == val:
                    j += 1
                if j != n:
                    nums[i], nums[j] = nums[j], nums[i]
            i += 1
        i = 0
        count = 0
        while i < n:
            if nums[i] == val:
                count += 1
                nums[i] = '_'
            i += 1
        return n-count
class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[List[int]]:
        res = []
        n = len(nums)

        # Edge case:
        if lower == upper and n > 0:
            return res
        
        if n == 0:
            return [[lower, upper]]

        if n == 1:
            if nums[0] == upper:
                res.append([lower, upper - 1])
            elif nums[0] == lower:
                res.append([lower + 1, upper])
            else:
                res.append([lower, nums[0] - 1])
                res.append([nums[0] + 1, upper])
            return res

        i = 0
        curr = lower
        if nums[i] != lower:
            res.append([lower, nums[i] - 1])
            curr = nums[0]
        while i < n-1:
            if nums[i+1] != nums[i] + 1:
                start = curr + 1
                end = nums[i+1] - 1
                res.append([start, end])
            
            i += 1
            curr = nums[i]

        if nums[i] < upper:
            res.append([nums[i] + 1, upper])

        return res
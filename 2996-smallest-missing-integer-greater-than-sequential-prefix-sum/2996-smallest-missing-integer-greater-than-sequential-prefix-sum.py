class Solution:
    def missingInteger(self, nums: List[int]) -> int:
        # More generic considering prefix can start from any index
        # maxLen = 1
        # total = nums[0]
        # maxTotal = nums[0]
        # n = len(nums)
        # i = 1
        # count = 1
        # while i < n:
        #     if nums[i-1] == nums[i] - 1:
        #         total += nums[i]
        #         count += 1
        #     else:
        #         total = nums[i]
        #         count = 1
        #     if count > maxLen:
        #         maxLen = count
        #         maxTotal = max(maxTotal, total)
        #     i += 1
        
        # while maxTotal in nums:
        #     maxTotal += 1
        
        # return maxTotal

        n = len(nums)
        total = nums[0]
        for j in range(1, n):
            if nums[j] != nums[j-1] + 1:
                break
            total += nums[j]
        
        while total in nums:
            total += 1
        
        return total
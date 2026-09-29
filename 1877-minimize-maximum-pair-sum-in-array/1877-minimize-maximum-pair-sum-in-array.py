class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        i, j = 0, n-1
        res = float('-inf')

        while i < j:
            pair_sum = nums[i] + nums[j]
            res = max(res, pair_sum)
            i += 1
            j -= 1
        
        return res
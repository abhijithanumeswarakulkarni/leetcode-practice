class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums.sort()
        n = len(nums)
        i, j = 0, n-1
        ops = 0

        while i < j:
            add = nums[i] + nums[j]
            if add == k:
                ops += 1
                i += 1
                j -= 1
            elif add < k:
                i += 1
            else:
                j -= 1
        
        return ops
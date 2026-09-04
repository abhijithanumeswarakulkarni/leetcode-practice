class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        maxPrefix = []
        minPostfix = []
        n = len(nums)
        mini, maxi = float('inf'), float('-inf')
        for i in range(n):
            maxi = max(maxi, nums[i])
            maxPrefix.append(maxi)
        for i in range(n-1, -1, -1):
            mini = min(mini, nums[i])
            minPostfix = [mini] + minPostfix
        
        for i in range(n):
            if maxPrefix[i] - minPostfix[i] <= k:
                return i
        return -1
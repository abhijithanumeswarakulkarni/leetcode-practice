class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        mini = float('inf')
        n = len(nums)
        l, r = 0, 0
        currSum = 0

        while r < n:
            currSum += nums[r]
            while currSum > target:
                mini = min(mini, (r-l+1))
                currSum -= nums[l]
                l += 1
            
            if currSum >= target:
                mini = min(mini, (r-l+1))
            r += 1
        
        return mini if mini != float('inf') else 0
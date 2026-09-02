class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        n = len(nums)

        if n == k:
            return sum(nums) / k

        l, r = 0, 0
        add = 0
        maxAvg = float('-inf')

        while r < n:
            while (r-l+1) > k:
                add -= nums[l]
                l += 1
            
            add += nums[r]
            
            if (r-l+1) == k:
                print(add)
                maxAvg = max(maxAvg, add / k)
            r += 1

        return maxAvg
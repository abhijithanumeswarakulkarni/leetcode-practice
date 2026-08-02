class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        # # Brute Force - Time = O(n^2), space = O(1) - TLE
        # n = len(nums)
        # res = 0
        # for i in range(n):
        #     total = 0
        #     for j in range(i, n):
        #         total += nums[j]
        #         if total > goal:
        #             break
        #         if total == goal:
        #             res += 1
        
        # return res

        # Prefix sum
        prefix_sum = 0
        res = 0
        hmap = {0: 1}
        n = len(nums)
        for i in range(n):
            prefix_sum += nums[i]
            if prefix_sum-goal in hmap:
                res += hmap[prefix_sum-goal]
            if prefix_sum in hmap:
                hmap[prefix_sum] += 1
            else:
                hmap[prefix_sum] = 1
        
        return res
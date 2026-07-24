class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # # Brute Force - Time = O(n^2), space = O(1) - TLE
        # n = len(nums)
        # for i in range(n-1):
        #     for j in range(i+1, n):
        #         if nums[i] == nums[j]:
        #             return True
        # return False

        # # Sort - Time = O(n*log(n)), space = O(1)
        # nums.sort()
        # n = len(nums)
        # for i in range(n-1):
        #     if nums[i] == nums[i+1]:
        #         return True
        # return False

        # Hashmap - Time = O(n), space = O(n)
        from collections import Counter
        hmap = Counter(nums)
        for key, val in hmap.items():
            if val > 1:
                return True
        return False

        # # Optimised hmap - Same complexities as above but skips full iteration
        # hmap = {}
        # for num in nums:
        #     if num in hmap:
        #         return True
        #     hmap[num] = 1
        # return False
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # # Brute Force - Time = O(n^2), space = O(1) - TLE
        # n = len(nums)
        # for i in range(n-1):
        #     for j in range(i+1, n):
        #         if nums[i] == nums[j]:
        #             return True
        # return False

        # Hashmap - Time = O(n), space = O(n)
        hmap = {}
        for num in nums:
            if num in hmap:
                hmap[num] += 1
            else:
                hmap[num] = 1
        for key, val in hmap.items():
            if val > 1:
                return True
        return False
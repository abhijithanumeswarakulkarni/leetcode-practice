class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # # Brute force - Time = O(n^2), space = O(1)
        # n = len(nums)
        # for i in range(n-1):
        #     for j in range(i+1, n):
        #         if nums[i] + nums[j] == target:
        #             return [i, j]
        # return [-1, -1] # Never reached according to desc

        # Hmap
        hmap = {}
        for index, num in enumerate(nums):
            if target-num in hmap:
                return [index, hmap[target-num]]
            else:
                hmap[num] = index
        return [-1, -1] # Never reached
        
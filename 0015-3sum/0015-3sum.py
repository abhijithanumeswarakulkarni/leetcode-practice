class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        # # Brute force - Time = O(n^3), space = O(1) - TLE
        # n = len(nums)
        # res = []
        # for i in range(n-2):
        #     for j in range(i+1, n-1):
        #         for k in range(j+1, n):
        #             three_sum = nums[i] + nums[j] + nums[k]
        #             elements = list(sorted([nums[i], nums[j], nums[k]]))
        #             if three_sum == 0 and elements not in res:
        #                 res.append(elements)
        # return res

        # Sorting - Time = O(n^2), space = O(1) - TLE
        nums.sort()
        res = []
        n = len(nums)
        for i in range(n-2):
            if nums[i] > 0:
                break
            if i != 0 and nums[i-1] == nums[i]:
                continue
            j = i+1
            k = n-1
            while j < k:
                add = nums[i] + nums[j] + nums[k]
                elements = [nums[i], nums[j], nums[k]]
                if add < 0:
                    j += 1
                elif add == 0:
                    res.append(elements)
                    j += 1
                    k -= 1
                    while j < k and nums[j-1] == nums[j]:
                        j += 1
                else:
                    k -= 1
        return res

        # # Fixing one + two sum with hmap - TLE
        # res = []
        # n = len(nums)
        # for i in range(n):
        #     target = -nums[i]
        #     other_elements = nums[:i] + (nums[i+1:] if i+1 < n else [])
        #     hmap = {}
        #     for ele in other_elements:
        #         if target-ele in hmap:
        #             elements = list(sorted([nums[i], target-ele, hmap[target-ele]]))
        #             if elements not in res:
        #                 res.append(elements)
        #         else:
        #             hmap[ele] = target-ele
        # return res
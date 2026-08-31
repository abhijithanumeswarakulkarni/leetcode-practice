class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        # # Brute force - TLE
        # n = len(nums)
        # res = []
        # for i in range(n-3):
        #     for j in range(i+1, n-2):
        #         for k in range(j+1, n-1):
        #             currSum = nums[i] + nums[j] + nums[k]
        #             targetEle = target - currSum
        #             for l in range(k+1, n):
        #                 if nums[l] == targetEle:
        #                     sortedElements = list(sorted([nums[i], nums[j], nums[k], nums[l]]))
        #                     if sortedElements not in res:
        #                         res.append(sortedElements)
        # return res

        # Hmap
        n = len(nums)

        # Edge cases
        if n < 4:
            return []
        
        if n == 4:
            return [nums] if sum(nums) == target else []

        hmap = {}
        for index, ele in enumerate(nums):
            hmap[ele] = index
        
        res = []
        for i in range(n-3):
            for j in range(i+1, n-2):
                for k in range(j+1, n-1):
                    currSum = nums[i] + nums[j] + nums[k]
                    targetEle = target - currSum
                    if targetEle in hmap:
                        targetIndex = hmap[targetEle]
                        if targetIndex != i and targetIndex != j and targetIndex != k:
                            sortedElements = list(sorted([nums[i], nums[j], nums[k], nums[targetIndex]]))
                            if sortedElements not in res:
                                res.append(sortedElements)
        return res
class Solution:
    def maximumMatchingIndices(self, nums1: List[int], nums2: List[int]) -> int:
        res = 0
        n = len(nums1)

        for idx in range(n):
            shifted_nums1 = nums1[idx:] + nums1[:idx]
            count = 0
            for index, value in enumerate(shifted_nums1):
                if value == nums2[index]:
                    count += 1
            res = max(res, count)
        
        return res
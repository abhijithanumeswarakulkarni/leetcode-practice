class Solution:
    def minProductSum(self, nums1: List[int], nums2: List[int]) -> int:
        sorted_nums1 = reversed(list(sorted(nums1)))
        sorted_nums2 = list(sorted(nums2))
        res = 0
        for index, value in enumerate(sorted_nums1):
            res += value * sorted_nums2[index]
        return res
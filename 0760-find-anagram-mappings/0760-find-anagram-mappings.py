class Solution:
    def anagramMappings(self, nums1: list[int], nums2: list[int]) -> list[int]:
        nums2_index = {}
        for index, value in enumerate(nums2):
            if value not in nums2_index:
                nums2_index[value] = [index]
            else:
                nums2_index[value].append(index)
        
        n = len(nums1)
        res = [-1] * n

        for index, value in enumerate(nums1):
            nums2_idx = nums2_index[value].pop(0)
            res[index] = nums2_idx
        
        return res
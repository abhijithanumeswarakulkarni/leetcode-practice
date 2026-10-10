import math

class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        # # Not ideal - Time = O(m+n * log(m + n))
        # all_nums = list(sorted(nums1 + nums2))
        # total = len(nums1) + len(nums2)
        # if total % 2 == 0:
        #     return (all_nums[total // 2] + all_nums[total // 2 - 1]) / 2
        # return all_nums[total // 2]

        m, n = len(nums1), len(nums2)
        total_len = m + n
        # If total_len even -> avg of mid and mid + 1
        # Odd -> mid
        i, j = 0, 0
        while (i + j) < math.ceil(total_len / 2) - 1:
            if j == n or (i < m and nums1[i] < nums2[j]):
                i += 1
            else:
                j += 1
        print(i, j, total_len)

        if total_len % 2 == 0:
            if i < m and j < n:
                if i + 1 < m and nums1[i+1] < nums2[j]:
                    return (nums1[i] + nums1[i+1]) / 2
                
                if j + 1 < n and nums2[j+1] < nums1[i]:
                    return (nums2[j] + nums2[j+1]) / 2

                return (nums1[i] + nums2[j]) / 2
            elif i < m:
                return (nums1[i] + nums1[i+1]) / 2
            else:
                return (nums2[j] + nums2[j+1]) / 2
        else:
            if i < m and j < n:
                return min(nums1[i], nums2[j]) / 1
            elif i == m:
                return nums2[j] / 1
            else:
                return nums1[i] / 1
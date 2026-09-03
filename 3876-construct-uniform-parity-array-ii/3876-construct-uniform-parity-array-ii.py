class Solution:
    def uniformArray(self, nums1: list[int]) -> bool:
        # # Brute force - TLE
        # n = len(nums1)

        # # Odd loop
        # isOddPossible = True
        # for i in range(n):
        #     if nums1[i] % 2 == 0:
        #         canHappen = False
        #         for j in range(n):
        #             diff = nums1[i] - nums1[j]
        #             if j != i and diff >= 1 and (diff) % 2 != 0:
        #                 canHappen = True
        #                 break
        #         if not canHappen:
        #             isOddPossible = False
        #             break
        # if isOddPossible:
        #     return True
        
        # # Even loop
        # isEvenPossible = True
        # for i in range(n):
        #     if nums1[i] % 2 != 0:
        #         canHappen = False
        #         for j in range(n):
        #             diff = nums1[i] - nums1[j]
        #             if j != i and diff >= 1 and (diff) % 2 == 0:
        #                 canHappen = True
        #                 break
        #         if not canHappen:
        #             isEvenPossible = False
        #             break
        # if isEvenPossible:
        #     return True
        
        # return False

        mn = nums1[0]
        hasOdd = False
        for v in nums1:
            if v < mn:
                mn = v
            if v % 2 != 0:
                hasOdd = True
        if mn % 2 != 0:
            return True
        return not hasOdd
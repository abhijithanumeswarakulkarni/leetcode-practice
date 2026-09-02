class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        # # Brute force - TLE
        # n = len(nums)
        # for i in range(n-2):
        #     for j in range(i+1, n-1):
        #         for k in range(j+1, n):
        #             if nums[i] < nums[j] and nums[j] < nums[k]:
        #                 return True
        # return False

        # 2 Pointers with middle element fixed
        n = len(nums)
        maxi = max(nums)
        mini = min(nums)
        for i in range(1, n-1):
            if nums[i] == mini or nums[i] == maxi:
                continue

            hasLeft, hasRight = False, False
            for k in range(i):
                if nums[k] < nums[i]:
                    hasLeft = True
                    break
            for k in range(i+1, n):
                if nums[i] < nums[k]:
                    hasRight = True
                    break
            
            if hasLeft and hasRight:
                return True

        return False

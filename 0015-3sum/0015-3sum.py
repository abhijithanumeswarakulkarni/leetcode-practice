class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        n = len(nums)
        nums.sort()
        res = []
        i = 1
        for i in range(n-2):
            if nums[i] > 0:
                break
            if i != 0 and nums[i-1] == nums[i]:
                continue
            j = i+1
            k = n-1
            while j < k:
                add = nums[i] + nums[j] + nums[k]
                ele = [nums[i], nums[j], nums[k]]
                if add < 0:
                    j += 1
                elif add > 0:
                    k -= 1
                else:
                    res.append(ele)
                    j += 1
                    k -= 1
                    while j < k and nums[j-1] == nums[j]:
                        j += 1
            i += 1
        return res
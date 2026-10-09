class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        n = len(nums)
        res = []

        for i in range(n-2):
            if nums[i] > 0:
                break
            if i > 0 and nums[i] == nums[i-1]:
                continue
            j, k = i + 1, n - 1
            while j < k:
                curr_sum = nums[i] + nums[j] + nums[k]
                curr_ele = [nums[i], nums[j], nums[k]]
                if curr_sum == 0:
                    res.append([nums[i], nums[j], nums[k]])
                    j += 1
                    k -= 1
                    while j < k and nums[j-1] == nums[j]:
                        j += 1
                elif curr_sum > 0:
                    k -= 1
                else:
                    j += 1
        
        return res
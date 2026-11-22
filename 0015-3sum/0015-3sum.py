class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        i = 0
        n = len(nums)
        res = []

        while i < n - 2:
            if nums[i] > 0:
                break

            j = i + 1
            k = n - 1

            while j < k:
                tripl_sum = nums[i] + nums[j] + nums[k]
                if tripl_sum == 0:
                    res.append([nums[i], nums[j], nums[k]])
                    while j < k and nums[j] == nums[j + 1]:
                        j += 1
                    j += 1
                    k -= 1
                elif tripl_sum < 0:
                    j += 1
                else:
                    k -= 1
            
            while i < n - 1 and nums[i] == nums[i+1]:
                i += 1
            i += 1
        
        return res
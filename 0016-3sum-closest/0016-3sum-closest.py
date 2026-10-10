class Solution:
    def threeSumClosest(self, nums: list[int], target: int) -> int:
        nums.sort()
        n = len(nums)
        mini = float('inf')
        res = 0

        for i in range(n-2):
            j, k = i+1, n-1
            while j < k:
                curr_sum = nums[i] + nums[j] + nums[k]
                diff = target - curr_sum
                if abs(diff) < mini:
                    res = curr_sum
                    mini = abs(diff)

                if diff < 0:
                    k -= 1
                else:
                    j += 1
        
        return res
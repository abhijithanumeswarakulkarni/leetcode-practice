class Solution:
    def peakValleyDifference(self, nums: list[int]) -> int:
        peaks_sum, valleys_sum = 0, 0
        n = len(nums)

        for i in range(1, n-1):
            if nums[i] > nums[i+1] and nums[i] > nums[i-1]:
                peaks_sum += nums[i]
            if nums[i] < nums[i+1] and nums[i] < nums[i-1]:
                valleys_sum += nums[i]
        
        return peaks_sum - valleys_sum
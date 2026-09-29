class Solution:
    def maxSum(self, nums: List[int], threshold: List[int]) -> int:
        nums_and_threshold = []
        
        for index, num in enumerate(nums):
            nums_and_threshold.append((threshold[index], num))
        
        nums_and_threshold = list(sorted(nums_and_threshold, key=lambda x: (x[0], -x[1])))
        
        total = 0
        for step, value in enumerate(nums_and_threshold):
            if value[0] > (step + 1):
                break
            total += value[1]
        
        return total
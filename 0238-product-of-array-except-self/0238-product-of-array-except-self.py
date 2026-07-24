class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # left + right array
        n = len(nums)
        left, right = [1] * n, [1] * n
        
        for index in range(1, n):
            left[index] = left[index-1] * nums[index-1]
        
        for index in range(n-2, -1, -1):
            right[index] = right[index+1] * nums[index+1]
        
        result = []
        for index in range(n):
            result.append(left[index] * right[index])

        return result
class Solution:
    def maxProduct(self, nums: list[int]) -> int:
        curr_prod, max_prod = 1, float('-inf')
        n = len(nums)

        for i in range(n):
            curr_prod *= nums[i]
            max_prod = max(max_prod, curr_prod)
            if curr_prod == 0:
                curr_prod = 1
        
        curr_prod = 1
        for i in range(n-1, -1, -1):
            curr_prod *= nums[i]
            max_prod = max(max_prod, curr_prod)
            if curr_prod == 0:
                curr_prod = 1
        
        return max_prod
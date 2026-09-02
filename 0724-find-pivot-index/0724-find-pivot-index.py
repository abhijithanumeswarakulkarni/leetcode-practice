class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        n = len(nums)
        prefix = [0] * n
        postfix = [0] * n
        for index in range(1, n):
            prefix[index] = prefix[index-1] + nums[index-1]
        for index in range(n-2, -1, -1):
            postfix[index] = postfix[index+1] + nums[index+1]
        
        for index in range(n):
            if prefix[index] == postfix[index]:
                return index
        
        return -1
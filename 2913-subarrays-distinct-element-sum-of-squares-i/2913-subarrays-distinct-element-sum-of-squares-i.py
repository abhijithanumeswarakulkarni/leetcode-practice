class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        # Bruteforce
        res = 0
        n = len(nums)
        for i in range(n):
            for j in range(i+1, n+1):
                distinct_count = len(set(nums[i:j]))
                res += distinct_count ** 2
        return res
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # Prefix sum (https://youtu.be/xvNwoz-ufXA?si=-EaCTCFfdDFNeBZ0)
        prefix_sum = 0
        res = 0
        hmap = {0: 1}
        n = len(nums)
        for i in range(n):
            prefix_sum += nums[i]
            if prefix_sum-k in hmap:
                res += hmap[prefix_sum-k]
            if prefix_sum in hmap:
                hmap[prefix_sum] += 1
            else:
                hmap[prefix_sum] = 1
        
        return res
class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        # # Brute force - Time = O(n^2), space = O(1) - TLE
        # n = len(nums)
        # res = 0
        # for i in range(n):
        #     for j in range(i+1, n+1):
        #         if sum(1 for x in nums[i:j] if x % 2 != 0) == k:
        #             res += 1
        # return res

        # Prefix sum (Similar to http://github.com/abhijithanumeswarakulkarni/leetcode-practice/blob/main/0930-binary-subarrays-with-sum/0930-binary-subarrays-with-sum.py)
        prefix_sum = 0
        hmap = {prefix_sum: 1}
        n = len(nums)
        res = 0

        for i in range(n):
            prefix_sum += nums[i] % 2
            if prefix_sum-k in hmap:
                res += hmap[prefix_sum-k]
            if prefix_sum in hmap:
                hmap[prefix_sum] += 1
            else:
                hmap[prefix_sum] = 1

        return res
class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        # # Brute force - Time = O(n^2), space = O(1) - TLE
        # n = len(nums)
        # res = 0
        # for i in range(n):
        #     for j in range(i+1, n+1):
        #         if len(set(nums[i:j])) == k:
        #             res += 1
        # return res

        # Sliding window - reconsier problem (https://youtu.be/7wYGbV_LsX4?si=y1r4WktrrfYz3pp7)
        n = len(nums)
        def solve(goal):
            l, r = 0, 0
            res = 0
            hmap = {}

            while r < n:
                if nums[r] in hmap:
                    hmap[nums[r]] += 1
                else:
                    hmap[nums[r]] = 1

                while len(hmap) > goal:
                    hmap[nums[l]] -= 1
                    if hmap[nums[l]] == 0:
                        del hmap[nums[l]]
                    l += 1
                res += sum(hmap.values())
                r += 1
            
            return res
        
        return solve(k) - solve(k-1)
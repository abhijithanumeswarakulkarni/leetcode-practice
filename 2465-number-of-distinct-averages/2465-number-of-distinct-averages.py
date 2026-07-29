class Solution:
    def distinctAverages(self, nums: List[int]) -> int:
        # Sort + set - Time = O(nlog(n)), space = O(n)
        nums.sort()
        avg = set()
        while nums:
            avg.add((nums[0] + nums[-1])/2)
            nums.pop(0)
            nums.pop(-1)
        return len(avg)
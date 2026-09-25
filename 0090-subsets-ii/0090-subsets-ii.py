class Solution:
    def subsetsWithDup(self, nums: list[int]) -> list[list[int]]:
        n = len(nums)
        res = []
        nums.sort()

        def solve(index, curr_set):
            if index == n:
                if curr_set not in res:
                    res.append(curr_set)
                return
            
            pick = solve(index+1, curr_set + [nums[index]])
            not_pick = solve(index+1, curr_set)

        solve(0, [])
        return res
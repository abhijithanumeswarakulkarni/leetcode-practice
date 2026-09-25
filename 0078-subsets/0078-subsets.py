class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        res = []
        n = len(nums)
        def solve(index, curr_set):
            if index == n:
                res.append(curr_set)
                return
            
            pick = solve(index+1, curr_set + [nums[index]])
            not_pick = solve(index+1, curr_set)
        
        solve(0, [])
        return res

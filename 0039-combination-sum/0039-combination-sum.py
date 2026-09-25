class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        n = len(candidates)
        res = []
        def solve(index, curr_set, curr_sum):
            if curr_sum == target:
                curr_set.sort()
                if curr_set not in res:
                    res.append(curr_set)
                return
            
            if index == n or curr_sum > target:
                return
            
            pick_move = solve(index+1, curr_set + [candidates[index]], curr_sum + candidates[index])
            pick_stay = solve(index, curr_set + [candidates[index]], curr_sum + candidates[index])
            not_pick = solve(index+1, curr_set, curr_sum)
        
        solve(0, [], 0)
        return res
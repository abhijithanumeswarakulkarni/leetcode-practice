class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        res = []
        n = len(candidates)

        def solve(index, curr_target, curr_elements):
            if curr_target == 0:
                if curr_elements not in res:
                    res.append(list(curr_elements))
                return
            
            if curr_target < 0 or index == n:
                return
            
            pick_move = solve(index + 1, curr_target - candidates[index], curr_elements + [candidates[index]])
            pick_stay = solve(index, curr_target - candidates[index], curr_elements + [candidates[index]])
            move = solve(index + 1, curr_target, curr_elements)
        
        solve(0, target, [])
        return res
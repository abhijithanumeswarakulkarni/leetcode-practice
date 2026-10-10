class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        n = len(candidates)
        candidates.sort()
        res = []

        def solve(index, remaining, curr_ele):
            nonlocal res

            if remaining == 0:
                if curr_ele not in res:
                    res.append(curr_ele)
                return

            if index == n or remaining < 0:
                return
            
            pick_move = solve(index + 1, remaining - candidates[index], curr_ele + [candidates[index]])
            pick_stay = solve(index, remaining - candidates[index], curr_ele + [candidates[index]])
            not_pick = solve(index + 1, remaining, curr_ele)
        
        solve(0, target, [])
        return res
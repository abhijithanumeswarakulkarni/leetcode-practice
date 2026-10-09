class Solution:
    def combinationSum2(self, candidates: list[int], target: int) -> list[list[int]]:
        res = []
        n = len(candidates)
        candidates.sort()

        def solve(index, curr_target, curr_elements):
            if curr_target == 0:
                if curr_elements not in res:
                    res.append(curr_elements)
                return
            
            if curr_target < 0 or index == n:
                return
            
            for i in range(index, n):
                if curr_target - candidates[i] < 0:
                    break
                
                if i > index and candidates[i] == candidates[i-1]:
                    continue
                
                pick = solve(i + 1, curr_target - candidates[i], curr_elements + [candidates[i]])
        
        solve(0, target, [])
        return res
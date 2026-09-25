class Solution:
    def combinationSum2(self, candidates: list[int], target: int) -> list[list[int]]:
        n = len(candidates)
        res = []
        total = sum(candidates)
        
        if total < target:
            return res
        
        if total == target:
            return [candidates]

        def solve(index, curr_set, curr_sum):
            if curr_sum == target:
                if curr_set not in res:
                    res.append(curr_set)
                return
            
            if index == n or curr_sum > target:
                return
            
            for i in range(index, n):
                if i > index and candidates[index] == candidates[i]:
                    continue
                
                if candidates[i] > target - curr_sum:
                    break
                
                solve(i+1, curr_set + [candidates[i]], curr_sum + candidates[i])
        
        candidates.sort()
        solve(0, [], 0)
        return res
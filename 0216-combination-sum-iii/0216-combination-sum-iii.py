class Solution:
    def combinationSum3(self, k: int, n: int) -> list[list[int]]:
        res = []

        def solve(index, curr_sum, curr_elements):
            if curr_sum == n:
                if index == k:
                    curr_elements.sort()
                    if curr_elements not in res:
                        res.append(curr_elements)
                return
            
            if curr_sum > n:
                return
            
            for num in range(1, 10):
                if curr_sum + num > n:
                    break
                
                if num in curr_elements:
                    continue
                
                pick = solve(index + 1, curr_sum + num, curr_elements + [num])
            
        solve(0, 0, [])
        return res
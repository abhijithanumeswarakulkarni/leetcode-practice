class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        res = []
        def solve(k, n, currEle):
            if n == 0 and k == 0:
                sortedCurrEle = list(sorted(currEle))
                if sortedCurrEle and sortedCurrEle not in res:
                    res.append(sortedCurrEle)
                return
            
            if k < 0:
                return
            
            for i in range(1, 10):
                if i not in currEle:
                    solve(k-1, n-i, currEle + [i])
        
        solve(k, n, [])
        return res
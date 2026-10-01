class Solution:
    def validStrings(self, n: int) -> List[str]:
        res = []

        def solve(curr_n, curr_str):
            if curr_n == 0:
                res.append(curr_str)
                return
            
            if not curr_str or curr_str[-1] != '0':
                solve(curr_n - 1, curr_str + '0')
            solve(curr_n - 1, curr_str + '1')

        solve(n, "")
        return res 
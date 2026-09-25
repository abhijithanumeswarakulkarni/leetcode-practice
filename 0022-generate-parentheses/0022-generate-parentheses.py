class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        res = []

        def isValid(par):
            stack = []
            for x in par:
                if x == '(':
                    stack.append(x)
                else:
                    if not stack or stack[-1] != '(':
                        return False
                    stack.pop()
            return True if not stack else False
        
        def solve(target, curr_par):
            if target == 0:
                if curr_par not in res and isValid(curr_par):
                    res.append(curr_par)
                return
            
            solve(target-1, curr_par + '(')
            solve(target-1, curr_par + ')')
        
        solve(2*n, "")
        return res
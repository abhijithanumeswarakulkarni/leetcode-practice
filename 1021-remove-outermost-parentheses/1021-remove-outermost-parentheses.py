class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        stack = []
        res = ""
        for x in s:
            if x == '(':
                if stack:
                    res += x
                stack.append(x)
            else:
                stack.pop()
                if stack:
                    res += x
        return res
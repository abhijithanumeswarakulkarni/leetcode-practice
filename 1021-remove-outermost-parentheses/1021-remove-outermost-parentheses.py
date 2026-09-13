class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        stack = []
        primitives = []
        temp = ""
        for x in s:
            if x == '(':
                temp += x
                stack.append(x)
            else:
                stack.pop()
                temp += x
            if not stack:
                primitives.append(temp)
                temp = ""

        res = ""
        for x in primitives:
            k = len(x)
            res += x[1:k-1]
        return res
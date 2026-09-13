class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        stack = []
        primitives = []
        temp = ""
        for x in s:
            if x == '(':
                if stack:
                    temp += x
                stack.append(x)
            else:
                stack.pop()
                if stack:
                    temp += x
            
        # print(temp)
        # res = ""
        # for x in primitives:
        #     k = len(x)
        #     res += x[1:k-1]
        # return res
        return temp
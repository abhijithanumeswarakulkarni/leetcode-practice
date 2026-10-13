class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = []
        for x in s:
            if x.isalpha() or x == '(':
                stack.append(x)
            else:
                temp = ""
                while stack[-1] != '(':
                    temp += stack.pop()
                stack.pop()
                for char in temp:
                    stack.append(char)
        return "".join(stack)
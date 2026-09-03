class Solution:
    def decodeString(self, s: str) -> str:
        stack = []

        for c in s:
            if c == ']':
                chars = ""
                while stack[-1] != '[':
                    chars = stack.pop() + chars
                stack.pop()
                num = ""
                while stack and stack[-1].isnumeric():
                    num = stack.pop() + num
                stack.append(chars * int(num))
            else:
                stack.append(c)
        
        return "".join(stack)
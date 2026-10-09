class Solution:
    def minInsertions(self, s: str) -> int:
        count = 0
        stack = []
        n = len(s)
        index = 0

        while index < n:
            char = s[index]
            if char == '(':
                stack.append(char)
                index += 1
            else:
                if index + 1 < n and s[index + 1] == ')':
                    if stack and stack[-1] == '(':
                        stack.pop()
                    else:
                        count += 1
                    index += 2
                else:
                    if stack:
                        stack.pop()
                        count += 1
                    else:
                        count += 2
                    index += 1
        
        count += len(stack) * 2
        return count
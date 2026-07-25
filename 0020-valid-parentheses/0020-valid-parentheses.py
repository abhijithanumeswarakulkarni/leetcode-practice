class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        operators = {')': '(', '}': '{', ']': '['}
        for x in s:
            if x in operators.values():
                stack.append(x)
            else:
                if not stack or stack.pop() != operators[x]:
                    return False
        return True if not stack else False
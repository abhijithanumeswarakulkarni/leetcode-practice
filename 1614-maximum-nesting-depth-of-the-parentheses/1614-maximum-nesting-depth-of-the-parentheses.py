class Solution:
    def maxDepth(self, s: str) -> int:
        max_depth = 0
        stack = []
        for x in s:
            if x == '(':
                stack.append(x)
            elif x == ')':
                stack.pop()
            max_depth = max(max_depth, len(stack))
        return max_depth
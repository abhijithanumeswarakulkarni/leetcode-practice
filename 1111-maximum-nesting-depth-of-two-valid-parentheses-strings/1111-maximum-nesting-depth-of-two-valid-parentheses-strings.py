class Solution:
    def maxDepthAfterSplit(self, seq: str) -> list[int]:
        max_depth = float('-inf')
        stack = []
        for x in seq:
            if x == '(':
                stack.append(x)
            else:
                stack.pop()
            
            max_depth = max(max_depth, len(stack))

        target = max_depth // 2
        stack = []
        res = []
        group = 0
        
        for x in seq:
            if x == '(':
                stack.append((x, group))
                if len(stack) > target and not group:
                    group = 1
                    stack.pop()
                    stack.append((x, group))
                res.append(group)
            else:
                popped = stack.pop()
                res.append(popped[1])
                if len(stack) < target:
                    group = 0
        
        return res
            
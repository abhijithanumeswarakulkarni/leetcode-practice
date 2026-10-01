class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        hmap = {'(': ')', '{': '}', '[': ']'}

        for x in s:
            if x == '(' or x == '{' or x == '[':
                stack.append(x)
            else:
                if not stack or hmap[stack[-1]] != x:
                    return False
                stack.pop()
        
        return True if not stack else False
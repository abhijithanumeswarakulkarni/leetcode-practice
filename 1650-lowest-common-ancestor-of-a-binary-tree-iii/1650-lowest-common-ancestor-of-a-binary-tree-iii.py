"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""

class Solution:
    def __init__(self):
        self.res = None
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        def traverse(node):
            if not node:
                return False
            
            left = traverse(node.left)
            right = traverse(node.right)
            mid = (p == node or q == node)

            if (left + right + mid) >= 2:
                self.res = node
            
            return left or right or mid
        
        root = p
        while root.parent:
            root = root.parent

        traverse(root)

        return self.res
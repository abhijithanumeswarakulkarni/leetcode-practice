# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    diff = float('inf')
    res = float('inf')
    def closestValue(self, root: TreeNode | None, target: float) -> int:
        def traverse(node):
            if not node:
                return
            
            diff = abs(node.val - target)
            if diff < self.diff:
                self.diff = diff
                self.res = node.val
            
            if diff == self.diff:
                self.res = min(self.res, node.val)

            traverse(node.left)
            traverse(node.right)

        traverse(root)
        return self.res
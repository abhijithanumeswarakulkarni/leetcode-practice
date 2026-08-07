# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    res = True
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def height(node):
            if not node:
                return 0
            
            left = height(node.left)
            right = height(node.right)

            if abs(right-left) > 1:
                self.res = False
            
            return 1 + max(left, right)
        
        height(root)
        return self.res
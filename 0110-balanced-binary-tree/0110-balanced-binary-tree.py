# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        INF = float('inf')
        
        def maxHeight(node):
            if not node:
                return 0
            
            left = maxHeight(node.left)
            right = maxHeight(node.right)

            if abs(left-right) > 1:
                return INF
            
            return 1 + max(left, right)

        return maxHeight(root) != INF
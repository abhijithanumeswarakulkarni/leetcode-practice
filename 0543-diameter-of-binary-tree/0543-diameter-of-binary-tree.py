# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    maxi = 0
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def height(node):
            if not node:
                return 0
            
            left = height(node.left)
            right = height(node.right)

            return 1 + max(left, right)
        
        def findMaxi(node):
            if not node:
                return
            
            leftHeight = height(node.left)
            rightHeight = height(node.right)

            self.maxi = max(self.maxi, leftHeight+rightHeight)
            findMaxi(node.left)
            findMaxi(node.right)
        
        findMaxi(root)
        return self.maxi
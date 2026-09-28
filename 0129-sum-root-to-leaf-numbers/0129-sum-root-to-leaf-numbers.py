# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    res = 0
    def sumNumbers(self, root: TreeNode | None) -> int:
        def traverse(node, curr):
            if not node:
                return
            
            if node and not node.left and not node.right:
                self.res += int(curr + str(node.val))
                return
            
            traverse(node.left, curr + str(node.val))
            traverse(node.right, curr + str(node.val))
        
        traverse(root, "")
        return self.res
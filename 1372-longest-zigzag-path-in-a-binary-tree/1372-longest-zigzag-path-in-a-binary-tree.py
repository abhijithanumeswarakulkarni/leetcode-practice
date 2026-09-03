# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    res = 0

    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        def dfs(node, direction, currHeight):
            if not node:
                return
            
            self.res = max(self.res, currHeight)
            updatedDirection = not direction
            if direction:
                dfs(node.left, updatedDirection, currHeight + 1)
                dfs(node.right, direction, 1)
            
            if not direction:
                dfs(node.right, updatedDirection, currHeight + 1)
                dfs(node.left, direction, 1)

        
        dfs(root, True, 0)
        
        return self.res
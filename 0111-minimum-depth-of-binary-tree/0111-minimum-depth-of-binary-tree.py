# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    res = float('inf')
    def minDepth(self, root: TreeNode | None) -> int:
        def dfs(node, depth):
            if not node:
                return
            
            if not node.left and not node.right:
                self.res = min(self.res, depth)

            dfs(node.left, depth+1)
            dfs(node.right, depth+1)
        
        dfs(root, 1)
        return self.res if self.res != float('inf') else 0
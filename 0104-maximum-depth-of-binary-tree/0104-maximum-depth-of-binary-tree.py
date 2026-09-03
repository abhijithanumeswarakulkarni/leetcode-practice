# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    maxDpt = 0

    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def dfs(node, currDepth):
            if not node:
                self.maxDpt = max(self.maxDpt, currDepth)
                return
            
            dfs(node.left, currDepth + 1)
            dfs(node.right, currDepth + 1)

        dfs(root, 0)
        return self.maxDpt
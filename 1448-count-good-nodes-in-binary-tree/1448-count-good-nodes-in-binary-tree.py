# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(node, currMax):
            if not node:
                return 0
            
            updatedMax = max(currMax, node.val)
            if node.val >= updatedMax:
                return 1 + dfs(node.left, updatedMax) + dfs(node.right, updatedMax)
            
            return dfs(node.left, updatedMax) + dfs(node.right, updatedMax)
        
        return dfs(root, root.val)
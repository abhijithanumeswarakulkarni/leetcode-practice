# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    res = 0
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(node, maxi):
            if not node:
                return
            
            if node.val >= maxi:
                self.res += 1    
                maxi = max(maxi, node.val)
            
            dfs(node.left, maxi)
            dfs(node.right, maxi)
        
        dfs(root, float(-inf))
        return self.res

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def identical(p, q):
            if (not p and not q):
                return True
            
            if (p and not q) or (not p and q) or (p.val != q.val):
                return False
            
            left = identical(p.left, q.left)
            right = identical(p.right, q.right)

            return left and right
        
        def dfs(node):
            if not node:
                return False

            res = False
            if node.val == subRoot.val:
                res = identical(node, subRoot)
            
            left = dfs(node.left)
            right = dfs(node.right)
            
            return res or left or right

        return dfs(root)
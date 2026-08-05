# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # # Recursion
        # res = []
        # def dfs(node):
        #     if not node:
        #         return
            
        #     dfs(node.left)
        #     res.append(node.val)
        #     dfs(node.right)
        
        # dfs(root)
        # return res

        # Iterative
        stack = []
        node = root
        res = []
        while True:
            if node:
                stack.append(node)
                node = node.left
                continue
            
            if not stack:
                break
            
            node = stack.pop()
            res.append(node.val)
            node = node.right
            
        return res
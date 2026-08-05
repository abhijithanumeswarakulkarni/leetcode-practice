# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # # Recursive
        # es = []
        # def dfs(node):
        #     if not node:
        #         return
            
        #     dfs(node.left)
        #     dfs(node.right)
        #     res.append(node.val)
        
        # dfs(root)
        # return res

        # Iterative - 2 stacks
        stack1 = [root]
        stack2 = []

        while stack1:
            node = stack1.pop()
            if node:
                stack2.append(node)
                if node.left:
                    stack1.append(node.left)
                if node.right:
                    stack1.append(node.right)
        
        res = []
        while stack2:
            res.append(stack2.pop().val)
        
        return res
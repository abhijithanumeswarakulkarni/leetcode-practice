# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        def dfs(node, target, canStart):
            if not node:
                return 0
                
            op1 = 0
            if target-node.val == 0:
                op1 = 1 + dfs(node.left, target-node.val, False) + dfs(node.right, target-node.val, False)
            else:         
                op1 = dfs(node.left, target-node.val, False) + dfs(node.right, target-node.val, False)
            op2 = 0
            if canStart:
                op2 = dfs(node.left, target, True) + dfs(node.right, target, True)

            return op1 + op2
        
        return dfs(root, targetSum, True)
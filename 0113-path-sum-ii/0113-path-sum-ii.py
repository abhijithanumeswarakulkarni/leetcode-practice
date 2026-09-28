# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: TreeNode | None, targetSum: int) -> list[list[int]]:
        res = []

        def traverse(node, temp, curr_sum):
            if not node:
                return

            if node and not node.left and not node.right:
                if node.val + curr_sum == targetSum:
                    res.append(temp + [node.val])
                return
            
            traverse(node.left, temp + [node.val], curr_sum + node.val)
            traverse(node.right, temp + [node.val], curr_sum + node.val)
        
        traverse(root, [], 0)
        return res
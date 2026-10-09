# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: TreeNode | None) -> int:
        total = 0
        def traverse(node, parent, grand_parent):
            nonlocal total
            if not node:
                return
            
            if grand_parent and grand_parent.val % 2 == 0:
                total += node.val
            
            traverse(node.left, node, parent)
            traverse(node.right, node, parent)

        traverse(root, None, None)
        return total
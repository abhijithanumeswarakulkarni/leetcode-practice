# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.res = 0

    def sumEvenGrandparent(self, root: TreeNode | None) -> int:
        def traverse(node, parent, grand_parent):
            if not node:
                return
            
            if grand_parent and grand_parent % 2 == 0:
                self.res += node.val
            
            traverse(node.left, node.val, parent)
            traverse(node.right, node.val, parent)

        traverse(root, None, None)
        return self.res
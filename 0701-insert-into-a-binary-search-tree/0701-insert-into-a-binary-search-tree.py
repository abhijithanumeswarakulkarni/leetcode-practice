# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: TreeNode | None, val: int) -> TreeNode | None:
        # Edge case
        def traverse(node):
            if not node:
                return TreeNode(val)
            
            if val < node.val:
                left = traverse(node.left)
                if left:
                    node.left = left
                    return
            
            if val > node.val:
                right = traverse(node.right)
                if right:
                    node.right = right
                    return
            
        res = traverse(root)
        return root if not res else res
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def reverseOddLevels(self, root: TreeNode | None) -> TreeNode | None:
        levels = {}
        
        def traverse(node, level):
            if not node:
                return
            
            if level in levels:
                levels[level].append(node.val)
            else:
                levels[level] = [node.val]
            
            traverse(node.left, level + 1)
            traverse(node.right, level + 1)
        
        def update(node, level):
            if not node:
                return
            
            if level % 2 != 0:
                node.val = levels[level].pop()
            update(node.left, level + 1)
            update(node.right, level + 1)
        
        traverse(root, 0)
        update(root, 0)
        return root
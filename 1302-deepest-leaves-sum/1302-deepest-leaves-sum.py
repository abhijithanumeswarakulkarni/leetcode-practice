# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: TreeNode | None) -> int:
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
        
        traverse(root, 0)
        deepest_level = max(levels.keys())
        return sum(levels[deepest_level])
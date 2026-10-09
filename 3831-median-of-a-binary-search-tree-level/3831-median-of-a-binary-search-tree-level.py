# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelMedian(self, root: Optional[TreeNode], level: int) -> int:
        levels = {}

        def traverse(node, lvl):
            if not node:
                return
            
            if lvl in levels:
                levels[lvl].append(node.val)
            else:
                levels[lvl] = [node.val]
            
            traverse(node.left, lvl + 1)
            traverse(node.right, lvl + 1)
        
        traverse(root, 0)

        if level not in levels:
            return -1
        
        nodes = levels[level]
        n = len(nodes)

        if n % 2 != 0:
            return nodes[n // 2]
        
        return max(nodes[n // 2], nodes[(n // 2) - 1])
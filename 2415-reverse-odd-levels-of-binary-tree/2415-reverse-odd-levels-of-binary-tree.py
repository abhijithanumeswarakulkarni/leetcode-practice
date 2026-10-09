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
                levels[level].append(node)
            else:
                levels[level] = [node]
            
            num_nodes = len(levels[level])
            if level % 2 != 0 and num_nodes == 2 ** level:
                nodes = levels[level]
                for index in range(num_nodes//2):
                    nodes[index].val, nodes[num_nodes - index - 1].val = nodes[num_nodes - index - 1].val, nodes[index].val
            
            traverse(node.left, level + 1)
            traverse(node.right, level + 1)
        
        traverse(root, 0)
        return root
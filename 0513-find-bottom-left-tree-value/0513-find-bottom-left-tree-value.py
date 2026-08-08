# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        levels = []
        def bfs(node, lvl):
            if not node:
                return
            
            if lvl >= len(levels):
                levels.append([node.val])
            else:
                levels[lvl].append(node.val)
            
            bfs(node.left, lvl+1)
            bfs(node.right, lvl+1)

        bfs(root, 0)
        
        return levels[-1][0]
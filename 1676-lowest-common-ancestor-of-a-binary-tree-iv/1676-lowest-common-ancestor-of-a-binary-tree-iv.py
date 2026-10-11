# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def __init__(self):
        self.res = None

    def lowestCommonAncestor(self, root: 'TreeNode', nodes: 'List[TreeNode]') -> 'TreeNode':
        nodes = set(nodes)
        k = len(nodes)

        def traverse(node):
            if not node:
                return 0
            
            left = traverse(node.left)
            right = traverse(node.right)
            mid = node in nodes

            if (left + right + mid) == k and not self.res:
                self.res = node
            
            return left + right + mid
        
        traverse(root)

        return self.res
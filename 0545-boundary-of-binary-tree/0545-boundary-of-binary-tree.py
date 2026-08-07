# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def boundaryOfBinaryTree(self, root: Optional[TreeNode]) -> List[int]:
        if not root.left and not root.right:
            return [root.val]
        
        leftBound = []
        leafBound = []
        rightBound = []

        # Left
        node = root.left
        while node:
            if node.left or node.right:
                leftBound.append(node.val)
            if node.left:
                node = node.left
            else:
                node = node.right
        

        # Leaf nodes
        def dfs(node):
            if not node:
                return
            
            if not node.left and not node.right:
                leafBound.append(node.val)
            

            dfs(node.left)
            dfs(node.right)
        dfs(root)
        
        # Right
        node = root.right
        while node:
            if node.left or node.right:
                rightBound.append(node.val)
            if node.right:
                node = node.right
            else:
                node = node.left
        rightBound = rightBound[::-1]

        return [root.val] + leftBound + leafBound + rightBound
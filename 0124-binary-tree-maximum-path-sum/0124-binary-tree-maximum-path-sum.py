# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    res = float('-inf')
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        def traverse(node):
            if not node:
                return 0
            
            leftSum = traverse(node.left)
            rightSum = traverse(node.right)
            currVal = node.val
            maxPossible = max(currVal + leftSum, currVal + rightSum, currVal)
            self.res = max(self.res, maxPossible, currVal + leftSum + rightSum)

            return maxPossible

        traverse(root)
        return self.res
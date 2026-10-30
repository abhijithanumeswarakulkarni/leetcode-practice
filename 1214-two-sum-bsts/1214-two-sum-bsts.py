# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def twoSumBSTs(self, root1: TreeNode | None, root2: TreeNode | None, target: int) -> bool:
        # def traverse(node1, node2):
        #     if not node1 or not node2:
        #         return False
            
        #     if node1.val + node2.val == target:
        #         return True
            
        #     res = traverse(node1.left, node2) or traverse(node1.right, node2) or traverse(node1, node2.left) or traverse(node1, node2.right)

        #     return res
        
        # return traverse(root1, root2)

        compliment = []
        def traverse(node, check):
            if not node:
                return False
            
            if not check:
                compliment.append(target - node.val)
            else:
                if node.val in compliment:
                    return True
            
            left = traverse(node.left, check)
            right = traverse(node.right, check)

            return left or right
        
        traverse(root1, False)
        return traverse(root2, True)
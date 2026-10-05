# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class FindElements:

    def __init__(self, root: TreeNode | None):
        self.root = root

        def traverse(node, val):
            if not node:
                return
            
            node.val = val
            traverse(node.left, 2 * val + 1)
            traverse(node.right, 2 * val + 2)
        
        traverse(root, 0)

    def find(self, target: int) -> bool:
        def traverse(node):
            if not node:
                return False
            
            if node.val == target:
                return True
            
            left = traverse(node.left)
            right = traverse(node.right)

            return left or right
        
        return traverse(self.root)

# Your FindElements object will be instantiated and called as such:
# obj = FindElements(root)
# param_1 = obj.find(target)
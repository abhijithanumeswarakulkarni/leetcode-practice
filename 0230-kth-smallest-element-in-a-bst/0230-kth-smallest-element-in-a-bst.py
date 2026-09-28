# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: TreeNode | None, k: int) -> int:
        # Brute force
        heap = []

        def dfs(node):
            if not node:
                return
            
            heapq.heappush(heap, node.val)
            dfs(node.left)
            dfs(node.right)
        
        dfs(root)

        res = root.val
        while k > 0:
            res = heapq.heappop(heap)
            k -= 1
        
        return res
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        hmap = {}
        def dfs(node, row, col):
            if not node:
                return
            
            if col in hmap:
                hmap[col].append((node.val, row))
            else:
                hmap[col] = [(node.val, row)]
            
            dfs(node.left, row+1, col-1)
            dfs(node.right, row+1, col+1)
        
        dfs(root, 0, 0)

        sortedItems = sorted(hmap.items(), key=lambda x: x[0])
        temp = [sorted(item[1], key=lambda x: (x[1], x[0])) for item in sortedItems]
        res = []
        for x in temp:
            t = []
            for y in x:
                t.append(y[0])
            res.append(t)

        return res
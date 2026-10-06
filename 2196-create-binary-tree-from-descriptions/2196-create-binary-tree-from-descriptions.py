# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def createBinaryTree(self, descriptions: list[list[int]]) -> TreeNode | None:
        hmap = {}
        for parent, child, is_left in descriptions:
            if parent not in hmap:
                hmap[parent] = {'left': None, 'right': None, 'is_root': True}
            if is_left:
                hmap[parent]['left'] = child
            else:
                hmap[parent]['right'] = child
        
        for _, child, _ in descriptions:
            if child in hmap:
                hmap[child]['is_root'] = False
        
        root_val = None
        for key in hmap:
            if hmap[key]['is_root']:
                root_val = key
                break

        root = TreeNode(root_val)
        queue = deque([root])
        while queue:
            pop = queue.popleft()
            key = pop.val
            
            if key in hmap and hmap[key]['left']:
                childNode = TreeNode(hmap[key]['left'])
                pop.left = childNode
                queue.append(childNode)
            
            if key in hmap and hmap[key]['right']:
                childNode = TreeNode(hmap[key]['right'])
                pop.right = childNode
                queue.append(childNode)

        return root
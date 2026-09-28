"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        hmap = {}
        def bfs(node, level):
            if not node:
                return
            
            if level in hmap:
                hmap[level].append(node)
            else:
                hmap[level] = [node]
            
            bfs(node.left, level + 1)
            bfs(node.right, level + 1)
        
        bfs(root, 0)
        
        for key in hmap:
            nodes = hmap[key]
            n = len(nodes)
            for index in range(0, n-1):
                nodes[index].next = nodes[index+1]
        
        return root
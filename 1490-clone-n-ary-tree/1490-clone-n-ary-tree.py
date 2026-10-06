"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children if children is not None else []
"""

class Solution:
    def cloneTree(self, root: 'Node') -> 'Node':
        if not root:
            return root
            
        cloned_root = None
        queue = deque([root])
        hmap = {}

        while queue:
            curr = queue.popleft()
            new_node = Node(curr.val)


            for child in curr.children:
                queue.append(child)
                hmap[child] = new_node
            
            if not cloned_root:
                cloned_root = new_node

            if curr in hmap:
                hmap[curr].children.append(new_node)

        return cloned_root
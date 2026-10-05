"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        visited = {}

        def clone(graph_node):
            if not graph_node:
                return None
            
            if graph_node in visited:
                return visited[graph_node]
            
            new_node = Node(graph_node.val, [])
            visited[graph_node] = new_node
            if graph_node.neighbors:
                new_node.neighbors = [clone(nbr) for nbr in graph_node.neighbors]
            
            return new_node
        
        return clone(node)
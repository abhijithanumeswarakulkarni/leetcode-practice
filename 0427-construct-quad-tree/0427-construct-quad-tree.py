"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        n = len(grid)

        def build(i, j, curr_n):
            if curr_n == 1:
                return Node(1 if grid[i][j] == 1 else 0, True)
            
            k = curr_n // 2
            
            # Top Left
            top_left = 0
            for x in range(i, i + k):
                for y in range(j, j + k):
                    top_left += grid[x][y]
            top_left_node = None
            if top_left == k * k or top_left == 0:
                top_left_node = Node(1 if top_left == k * k else 0, True)
            else:
                top_left_node = build(i, j, k)
            
            # Top Right
            top_right = 0
            for x in range(i, i + k):
                for y in range(j + k, j + curr_n):
                    top_right += grid[x][y]
            top_right_node = None
            if top_right == k * k or top_right == 0:
                top_right_node = Node(1 if top_right == k * k else 0, True)
            else:
                top_right_node = build(i, j + k, k)
            
            # Bottom Left
            bottom_left = 0
            for x in range(i + k, i + curr_n):
                for y in range(j, j + k):
                    bottom_left += grid[x][y]
            bottom_left_node = None
            if bottom_left == k * k or bottom_left == 0:
                bottom_left_node = Node(1 if bottom_left == k * k else 0, True)
            else:
                bottom_left_node = build(i + k, j, k)
            
            # Bottom Right
            bottom_right = 0
            for x in range(i + k, i + curr_n):
                for y in range(j + k, j + curr_n):
                    bottom_right += grid[x][y]
            bottom_right_node = None
            if bottom_right == k * k or bottom_right == 0:
                bottom_right_node = Node(1 if bottom_right == k * k else 0, True)
            else:
                bottom_right_node = build(i + k, j + k, k)

            new_node = None
            total_sum = top_left + top_right + bottom_left + bottom_right
            if total_sum == curr_n * curr_n or total_sum == 0:
                new_node = Node(total_sum // (curr_n * curr_n), True)
            else:
                new_node = Node(1, False, top_left_node, top_right_node, bottom_left_node, bottom_right_node)

            return new_node
        
        res = build(0, 0, n)
        return res
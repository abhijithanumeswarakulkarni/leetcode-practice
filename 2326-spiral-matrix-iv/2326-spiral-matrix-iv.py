# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def spiralMatrix(self, m: int, n: int, head: ListNode | None) -> list[list[int]]:
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        dir_index = 0
        visited = [[False] * n for _ in range(m)]
        grid = [[-1] * n for _ in range(m)]
        curr = head
        i, j = 0, 0
        while curr:
            grid[i][j] = curr.val
            visited[i][j] = True
            curr = curr.next
            direction = directions[dir_index]
            updated_i, updated_j = i + direction[0], j + direction[1]
            if updated_i < 0 or updated_i == m or updated_j < 0 or updated_j == n or visited[updated_i][updated_j]:
                dir_index = (dir_index + 1) % 4
                direction = directions[dir_index]
                updated_i, updated_j = i + direction[0], j + direction[1]
            i, j = updated_i, updated_j
        
        return grid
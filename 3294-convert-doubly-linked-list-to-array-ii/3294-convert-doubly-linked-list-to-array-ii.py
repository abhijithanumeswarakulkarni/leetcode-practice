"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev=None, next=None):
        self.val = val
        self.prev = prev
        self.next = next
"""
class Solution:
    def toArray(self, node: 'Optional[Node]') -> List[int]:
        res = []
        left = node
        right = node.next
        
        while left or right:
            if left:
                res = [left.val] + res
                left = left.prev
            if right:
                res.append(right.val)
                right = right.next

        return res
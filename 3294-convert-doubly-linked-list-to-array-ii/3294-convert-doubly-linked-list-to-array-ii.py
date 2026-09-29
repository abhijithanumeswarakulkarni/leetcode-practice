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
        curr = node
        while curr:
            res = [curr.val] + res
            curr = curr.prev
        curr = node.next
        while curr:
            res.append(curr.val)
            curr = curr.next
        return res
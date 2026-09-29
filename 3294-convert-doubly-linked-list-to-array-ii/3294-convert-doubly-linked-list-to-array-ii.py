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
        prev, nxt = [], []
        curr = node
        while curr:
            prev = [curr.val] + prev
            curr = curr.prev
        curr = node.next
        while curr:
            nxt.append(curr.val)
            curr = curr.next
        return prev + nxt
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev, curr = head, head.next

        while curr:
            mini = min(prev.val, curr.val)
            for x in range(mini, 0, -1):
                if prev.val % x == 0 and curr.val % x == 0:
                    new_node = ListNode(x)
                    prev.next = new_node
                    new_node.next = curr
                    break
            prev = curr
            curr = curr.next
        
        return head

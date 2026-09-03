# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow, fast, prev = head, head.next, None
        if not fast:
            return None

        while fast:
            if not fast.next:
                slow.next = slow.next.next
                return head
            prev = slow
            slow = slow.next
            fast = fast.next.next
        prev.next = slow.next
        
        return head
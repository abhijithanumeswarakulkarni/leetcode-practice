# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Edge case
        if not head or not head.next or not head.next.next:
            return head

        last = head
        count = 0
        while last.next:
            last = last.next
            count += 1
        count += 1

        curr = head
        index = 0
        while index < (count // 2):
            temp = curr.next
            curr.next = curr.next.next
            curr = curr.next
            last.next = temp
            last = temp
            last.next = None
            index += 1
        
        return head
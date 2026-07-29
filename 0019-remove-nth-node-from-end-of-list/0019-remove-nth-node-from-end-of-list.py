# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        count = 0
        temp = head
        while temp:
            count += 1
            temp = temp.next
        # Edge case
        if count == 1 and n == 1:
            return None
        pos_from_front = count - n
        if pos_from_front == 0:
            return head.next
            
        curr_pos = 0
        curr, prev = head, None
        while curr_pos < pos_from_front:
            prev = curr
            curr = curr.next
            curr_pos += 1
        prev.next = curr.next
        return head
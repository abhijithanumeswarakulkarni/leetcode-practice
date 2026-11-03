# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitCircularLinkedList(self, head: Optional[ListNode]) -> List[Optional[ListNode]]:
        if not head:
            return [None, None]

        slow, fast = head, head.next
        while fast.next != head and fast != head:
            slow = slow.next
            fast = fast.next.next
        
        second = slow.next
        slow.next = head
        temp = second
        while temp.next != head:
            temp = temp.next
        temp.next = second

        return [head, second]
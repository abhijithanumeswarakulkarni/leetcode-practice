# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: ListNode | None, x: int) -> ListNode | None:
        if not head or not head.next:
            return head
        
        less, great = None, None
        temp = head
        ltemp, rtemp = None, None
        
        while temp:
            if temp.val < x:
                if not less:
                    less = ListNode(temp.val)
                    ltemp = less
                else:
                    ltemp.next = ListNode(temp.val)
                    ltemp = ltemp.next
            else:
                if not great:
                    great = ListNode(temp.val)
                    rtemp = great
                else:
                    rtemp.next = ListNode(temp.val)
                    rtemp = rtemp.next
            temp = temp.next
        
        if not less:
            return great
        
        ltemp.next = great
        return less
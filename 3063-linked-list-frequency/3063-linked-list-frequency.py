# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def frequenciesOfElements(self, head: Optional[ListNode]) -> Optional[ListNode]:
        frq = {}
        temp = head
        
        while temp:
            key = temp.val
            if key in frq:
                frq[key] += 1
            else:
                frq[key] = 1
            temp = temp.next
        
        head, curr = None, None
        for key in frq:
            if not head:
                head = ListNode(frq[key])
                curr = head
            else:
                curr.next = ListNode(frq[key])
                curr = curr.next
        return head
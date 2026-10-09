# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: ListNode | None) -> ListNode | None:
        new_head, new_curr = None, None
        curr = head
        total = 0

        while curr:
            if curr.val == 0:
                if total != 0:
                    new_node = ListNode(total)
                    if not new_head:
                        new_head = new_node
                    else:
                        new_curr.next = new_node
                    new_curr = new_node
                total = 0
            else:
                total += curr.val
            curr = curr.next

        return new_head
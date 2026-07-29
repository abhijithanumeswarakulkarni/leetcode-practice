# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head or not head.next:
            return head
        
        count = 0
        temp, reverse = head, None
        while temp:
            if not reverse:
                reverse = ListNode(temp.val)
            else:
                new_node = ListNode(temp.val)
                new_node.next = reverse
                reverse = new_node
            temp = temp.next
            count += 1
        
        is_even = False
        if count % 2 == 0:
            count -= 1
            is_even = True
        
        curr1, nxt1, curr2, nxt2 = head, head.next, reverse, reverse.next
        for _ in range(count // 2):
            curr1.next = curr2
            curr2.next = nxt1
            curr1 = nxt1
            curr2 = nxt2
            nxt1 = curr1.next
            nxt2 = curr2.next
        
        if not is_even:
            curr1.next = None
        else:
            curr1.next.next = None
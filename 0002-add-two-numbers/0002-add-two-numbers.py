# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # In case it wasn't reversed already
        # def reverse(head):
        #     prev, curr, nxt = None, head, head.next
        #     while nxt:
        #         curr.next = prev
        #         prev = curr
        #         curr = nxt
        #         nxt = nxt.next
        #     return curr
        
        # reverse_l1 = reverse(l1)
        # reverse_l2 = reverse(l2)
        res = curr = None
        carry = 0
        while l1 and l2:
            add = (l1.val + l2.val + carry)
            new_node = ListNode(add % 10)
            carry = add // 10
            if curr:
                curr.next = new_node
                curr = new_node
            else:
                curr = res = new_node
            l1 = l1.next
            l2 = l2.next
        while l1:
            add = (l1.val + carry)
            carry = add // 10
            new_node = ListNode(add % 10)
            curr.next = new_node
            curr = new_node
            l1 = l1.next
        while l2:
            add = (l2.val + carry)
            carry = add // 10
            new_node = ListNode(add % 10)
            curr.next = new_node
            curr = new_node
            l2 = l2.next
        if carry != 0:
            new_node = ListNode(carry)
            curr.next = new_node
        return res
                
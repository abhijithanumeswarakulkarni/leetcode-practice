# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode | None, l2: ListNode | None) -> ListNode | None:
        t1, t2 = l1, l2
        res, curr = None, None
        carry = 0

        while t1 and t2:
            add = t1.val + t2.val + carry
            new_node = ListNode(add % 10)
            if curr:
                curr.next = new_node
            else:
                res = new_node
            curr = new_node
            carry = add // 10
            t1 = t1.next
            t2 = t2.next
        
        while t1:
            add = t1.val + carry
            new_node = ListNode(add % 10)
            curr.next = new_node
            curr = new_node
            carry = add // 10
            t1 = t1.next

        while t2:
            add = t2.val + carry
            new_node = ListNode(add % 10)
            curr.next = new_node
            curr = new_node
            carry = add // 10
            t2 = t2.next
        
        if carry > 0:
            new_node = ListNode(carry)
            curr.next = new_node
            
        return res
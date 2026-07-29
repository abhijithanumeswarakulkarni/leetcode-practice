# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # Two pointer
        # Edge case
        if not list1:
            return list2
        if not list2:
            return list1

        if list1.val > list2.val:
            list1, list2 = list2, list1
        
        curr1, curr2 = list1, list2
        while curr1.next and curr2.next:
            if curr1.next.val < curr2.val:
                curr1 = curr1.next
            else:
                temp1, temp2 = curr1.next, curr2.next
                curr1.next = curr2
                curr2.next = temp1
                curr1 = curr1.next
                curr2 = temp2
        
        if not curr1.next:
            curr1.next = curr2
        else:
            while curr1.next and curr1.next.val <= curr2.val:
                curr1 = curr1.next
            temp = curr1.next
            curr1.next = curr2
            curr2.next = temp
        
        return list1

                

        
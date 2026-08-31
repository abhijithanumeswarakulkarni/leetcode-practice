# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        # # Brute force - TLE
        # # Edge case
        # if not head or not head.next or not head.next.next:
        #     return [-1, -1]
        
        # temp = head
        # nodes = []
        # while temp:
        #     nodes.append(temp.val)
        #     temp = temp.next
        
        # i = 1
        # n = len(nodes)
        # criticalPoints = []
        # while i < n-1:
        #     if (nodes[i] < nodes[i-1] and nodes[i] < nodes[i+1]) or (nodes[i] > nodes[i-1] and nodes[i] > nodes[i+1]):
        #         criticalPoints.append((nodes[i], i))
        #     i += 1
        
        # mini = float('inf')
        # maxi = float('-inf')
        # k = len(criticalPoints)
        # for i in range(k-1):
        #     for j in range(i+1, k):
        #         mini = min(mini, abs(criticalPoints[j][1] - criticalPoints[i][1]))
        #         maxi = max(maxi, abs(criticalPoints[j][1] - criticalPoints[i][1]))
        # return [mini, maxi] if mini != float('inf') and maxi != float('-inf') else [-1, -1]

        # Edge case
        if not head or not head.next or not head.next.next:
            return [-1, -1]
        
        first, last = None, None
        prev, curr, nxt = head, head.next, head.next.next
        index = 1
        mini = float('inf')

        while nxt:
            if (curr.val < prev.val and curr.val < nxt.val) or (curr.val > prev.val and curr.val > nxt.val):
                if not first:
                    first = (curr, index)
                    last = (curr, index)
                else:
                    mini = min(mini, (index - last[1]))
                    last = (curr, index)
            index += 1
            prev = curr
            curr = nxt
            nxt = nxt.next
        
        return [mini, last[1] - first[1]] if first and last and first != last else [-1, -1]



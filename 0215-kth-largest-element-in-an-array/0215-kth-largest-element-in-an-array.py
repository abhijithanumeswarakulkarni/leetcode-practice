class Solution:
    def findKthLargest(self, nums: list[int], k: int) -> int:
        heap = []
        for num in nums:
            heapq.heappush(heap, -num)
        
        res = None
        while k > 0:
            res = -heapq.heappop(heap)
            k -= 1
        
        return res
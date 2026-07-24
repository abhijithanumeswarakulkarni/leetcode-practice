class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # # Count freq + Sort - Time = O(n*log(n)), space = O(n)
        # from collections import Counter
        # freq = Counter(nums)
        # freq = dict(sorted(freq.items(), key=lambda x: -x[1]))
        # return list(freq.keys())[:k]

        # Follow up - could use heap
        # heappush = O(log(n)), heappop = O(1), heapify = O(log(n))
        from collections import Counter
        import heapq
        freq = Counter(nums)
        heap = []
        for key, value in freq.items():
            heapq.heappush(heap, (-value, key))
        
        res = []
        while k > 0:
            res.append(heapq.heappop(heap)[1])
            k -= 1
        return res
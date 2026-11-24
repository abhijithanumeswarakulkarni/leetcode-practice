class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        frq = Counter(nums).items()
        rev_frq = [(-val, key) for key, val in frq]
        heapq.heapify(rev_frq)

        res = []
        for _ in range(k):
            _, val = heapq.heappop(rev_frq)
            res.append(val)
        
        return res
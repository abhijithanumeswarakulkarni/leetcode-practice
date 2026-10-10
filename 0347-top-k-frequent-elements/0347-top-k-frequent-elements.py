class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        frq = Counter(nums)
        heap = list(map(lambda item: (-item[1], item[0]), frq.items()))
        heapq.heapify(heap)
        res = []

        while k > 0:
            res.append(heapq.heappop(heap)[1])
            k -= 1
        
        return res
class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        frq = Counter(nums)
        
        # Option 1 - Time = O(n), space = O(n)
        # heap = list(map(lambda item: (-item[1], item[0]), frq.items()))
        # heapq.heapify(heap)
        # res = []

        # while k > 0:
        #     res.append(heapq.heappop(heap)[1])
        #     k -= 1
        
        # return res
        sorted_frq = list(sorted(frq.items(), key = lambda item: item[1], reverse = True))
        res = list(map(lambda item: item[0], sorted_frq[:k]))
        return res
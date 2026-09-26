class Solution:
    def lastStoneWeight(self, stones: list[int]) -> int:
        stones = list(map(lambda x: -x, stones))
        t = heapq.heapify(stones)
        while len(stones) > 1:
            stone1 = heapq.heappop(stones)
            stone2 = heapq.heappop(stones)
            if stone1 != stone2:
                heapq.heappush(stones, (stone1 - stone2))
        return -stones[0] if stones else 0
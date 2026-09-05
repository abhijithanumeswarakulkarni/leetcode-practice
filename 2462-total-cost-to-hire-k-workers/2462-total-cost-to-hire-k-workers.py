class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        n = len(costs)
        i, j = candidates, n-candidates-1
        totalCost = 0

        if i <= j:
            leftCands = costs[:candidates]
            rightCands = costs[n-candidates:]
            heapq.heapify(leftCands)
            heapq.heapify(rightCands)

            while k > 0 and i <= j:
                if leftCands[0] <= rightCands[0]:
                    totalCost += heapq.heappop(leftCands)
                    heapq.heappush(leftCands, costs[i])
                    i += 1
                else:
                    totalCost += heapq.heappop(rightCands)
                    heapq.heappush(rightCands, costs[j])
                    j -= 1
                k -= 1

            totalCands = leftCands + rightCands
            heapq.heapify(totalCands)
            while k > 0:
                totalCost += heapq.heappop(totalCands)
                k -= 1
        else:
            heapq.heapify(costs)
            while k > 0:
                totalCost += heapq.heappop(costs)
                k -= 1
        return totalCost
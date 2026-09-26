class Solution:
    def kClosest(self, points: list[list[int]], k: int) -> list[list[int]]:
        distance = []
        for point in points:
            distance.append((math.sqrt(point[0] ** 2 + point[1] ** 2), point[0], point[1]))
        
        heapq.heapify(distance)
        res = []
        while k:
            dist = heapq.heappop(distance)
            res.append([dist[1], dist[2]])
            k -= 1
        
        return res
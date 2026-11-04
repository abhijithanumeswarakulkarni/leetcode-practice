class Solution:
    def minimumAbsDifference(self, latencies: list[int]) -> list[list[int]]:
        min_diff = float('inf')
        n = len(latencies)
        latencies.sort()

        if n < 2:
            return []

        for i in range(n-1):
            diff = latencies[i+1] - latencies[i]
            min_diff = min(min_diff, diff)
        
        res = []
        for i in range(n-1):
            a, b = latencies[i], latencies[i+1]
            if b - a == min_diff:
                res.append([a, b])
        
        return res
class Solution:
    def findingUsersActiveMinutes(self, logs: list[list[int]], k: int) -> list[int]:
        frq = {}
        items = {}
        for key, value in logs:
            if key in items and value not in items[key]:
                items[key].append(value)
                frq[key] += 1
            if key not in items:
                items[key] = [value]
                frq[key] = 1
        
        res = [0] * k
        for _, value in frq.items():
            res[value-1] += 1
        
        return res        
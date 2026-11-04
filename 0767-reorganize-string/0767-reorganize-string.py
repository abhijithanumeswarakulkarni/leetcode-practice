class Solution:
    def reorganizeString(self, s: str) -> str:
        frq = Counter(s)
        heap = []

        for key, val in frq.items():
            heapq.heappush(heap, (-val, key))
        
        n = len(s)
        res = ""
        
        for _ in range(n):
            queue = deque()
            found = False
            while heap:
                frq, char = heapq.heappop(heap)
                if not res or (res and res[-1] != char):
                    found = True
                    res += char
                    frq += 1
                    if frq != 0:
                        heapq.heappush(heap, (frq, char))
                    break
                queue.append((frq, char))
            if not found:
                return ""
            while queue:
                heapq.heappush(heap, queue.popleft())
        
        return res
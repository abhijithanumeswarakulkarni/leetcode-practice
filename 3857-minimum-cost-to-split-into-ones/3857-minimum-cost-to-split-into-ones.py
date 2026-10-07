class Solution:
    def minCost(self, n: int) -> int:
        if n == 1:
            return 0
            
        queue = deque([n])
        total_cost = 0
        
        while queue:
            curr = queue.popleft()
            half = curr // 2
            a, b = half, curr - half
            total_cost += (a * b)
            if a != 1:
                queue.append(a)
            if b != 1:
                queue.append(b)
        
        return total_cost
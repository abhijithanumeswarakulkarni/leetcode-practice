class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        n = len(temperatures)
        res = [0] * n
        stack = [(temperatures[-1], n-1)]
        
        for idx in range(n-2, -1, -1):
            while stack and stack[-1][0] <= temperatures[idx]:
                stack.pop()
            
            if stack:
                res[idx] = stack[-1][1] - idx
                
            stack.append((temperatures[idx], idx))
        
        return res
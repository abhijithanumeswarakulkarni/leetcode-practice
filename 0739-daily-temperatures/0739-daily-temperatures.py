class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        n = len(temperatures)
        stack = [(temperatures[n-1], n-1)]
        res = [0] * n
        j = n - 2

        while j >= 0:
            while stack and temperatures[j] >= stack[-1][0]:
                stack.pop()
            if stack:
                res[j] = stack[-1][1] - j
            stack.append((temperatures[j], j))
            j -= 1
        
        return res
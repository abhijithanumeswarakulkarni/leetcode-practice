class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # # Brute force - Obv TLE
        # n = len(temperatures)
        # res = [0] * n
        # for i in range(n-1):
        #     for j in range(i+1, n):
        #         if temperatures[j] > temperatures[i]:
        #             res[i] = (j-i)
        #             break
        
        # return res

        # Stack
        n = len(temperatures)
        stack = [(temperatures[-1], n-1)]
        res = [0] * n
        for i in range(n-2, -1, -1):
            while stack and temperatures[i] >= stack[-1][0]:
                stack.pop()
            if stack:
                res[i] = stack[-1][1] - i
            stack.append((temperatures[i], i))
        return res
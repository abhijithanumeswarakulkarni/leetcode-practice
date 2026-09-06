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
        stack = [temperatures[-1]]
        n = len(temperatures)
        res = [0] * n
        for i in range(n-2, -1, -1):
            if temperatures[i] > stack[-1]:
                poppedElements = []
                while stack and temperatures[i] > stack[-1]:
                    poppedElements.append(stack.pop())
                if stack:
                    res[i] = len(poppedElements) + 1
                stack += poppedElements[::-1]
            else:
                res[i] = 1
            stack.append(temperatures[i])
        return res
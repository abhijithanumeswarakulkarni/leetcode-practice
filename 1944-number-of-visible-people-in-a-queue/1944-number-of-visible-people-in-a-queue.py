class Solution:
    def canSeePersonsCount(self, heights: list[int]) -> list[int]:
        # # Brute Force - TLE
        # n = len(heights)
        # res = [0] * n

        # for i in range(n-2, -1, -1):
        #     count = 1
        #     for j in range(i+2, n):
        #         min_height = min(heights[i], heights[j])
        #         max_height = max(heights[i+1:j])
        #         if min_height > max_height:
        #             count += 1
        #     res[i] = count
        
        # return res

        # # Brute Force - Optimised - TLE
        # n = len(heights)
        # res = [0] * n

        # for i in range(n-1):
        #     count = 0
        #     max_so_far = heights[i]
        #     for j in range(i+1, n):
        #         if (j == i + 1) or heights[j] > max_so_far:
        #             count += 1
        #             max_so_far = heights[j]
        #         if max_so_far > heights[i]:
        #             break
        #     res[i] = count
        
        # return res

        # Stack
        n = len(heights)
        stack = [heights[n-1]]
        res = [0] * n

        for i in range(n-2, -1, -1):
            height = heights[i]
            count = 0
            while stack and height > stack[-1]:
                stack.pop()
                count += 1
            if not stack:
                res[i] = count
            else:
                res[i] = count + 1
            stack.append(height)
        
        return res
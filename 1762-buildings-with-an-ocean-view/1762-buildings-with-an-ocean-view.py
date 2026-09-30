class Solution:
    def findBuildings(self, heights: list[int]) -> list[int]:
        res = []
        n = len(heights)
        max_height = float('-inf')

        for i in range(n-1, -1, -1):
            if heights[i] > max_height:
                res = [i] + res
                max_height = heights[i]
        
        return res
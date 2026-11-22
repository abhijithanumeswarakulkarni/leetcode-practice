class Solution:
    def maxArea(self, height: list[int]) -> int:
        n = len(height)
        i, j = 0, n - 1
        max_water = 0

        while i < j:
            max_water = max(max_water, (j - i) * min(height[i], height[j]))
            if height[i] < height[j]:
                i += 1
            else:
                j -= 1
        
        return max_water
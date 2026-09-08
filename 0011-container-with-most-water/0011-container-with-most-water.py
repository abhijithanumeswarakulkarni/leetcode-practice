class Solution:
    def maxArea(self, height: List[int]) -> int:
        maxi = float('-inf')
        n = len(height)
        i, j = 0, n-1
        while i < j:
            currArea = (j-i) * min(height[i], height[j])
            maxi = max(maxi, currArea)
            if height[i] < height[j]:
                i += 1
            else:
                j -= 1
        return maxi
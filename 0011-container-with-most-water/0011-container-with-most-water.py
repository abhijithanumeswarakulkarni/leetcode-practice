class Solution:
    def maxArea(self, height: List[int]) -> int:
        # # Brute Force - Time = O(n^2), space = O(n) - TLE
        # max_area = float('-inf')
        # n = len(height)
        # for left in range(n-1):
        #     for right in range(left+1, n):
        #         curr_area = (right-left) * min(height[left], height[right])
        #         max_area = max(max_area, curr_area)
        # return max_area

        # 2 Pointers - Time = O(n), space = O(1)
        left, right = 0, len(height)-1
        max_area = float('-inf')
        while left < right:
            curr_area = (right-left) * min(height[left], height[right])
            max_area = max(max_area, curr_area)
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return max_area
        
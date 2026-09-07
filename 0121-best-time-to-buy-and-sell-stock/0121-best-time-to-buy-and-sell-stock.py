class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # # Brute Force - Time = O(n^2), space = O(1) - TLE
        # n = len(prices)
        # maxi = 0
        # for i in range(n-1):
        #     for j in range(i+1, n):
        #         maxi = max(maxi, prices[j] - prices[i])
        # return maxi

        # Sliding window
        n = len(prices)
        l, r = 0, 1
        maxi = 0
        while r < n:
            while l < r and prices[r] <= prices[l]:
                l += 1
            
            if l < r:
                maxi = max(maxi, prices[r] - prices[l])
            
            r += 1
        return maxi
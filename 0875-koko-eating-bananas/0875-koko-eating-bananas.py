import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # # Brute Force = Time = O(n*k), space = O(1) -> k = max element in piles - TLE
        # for k in range(1, max(piles)+1):
        #     count = 0
        #     for pile in piles:
        #         count += math.ceil(pile / k)
        #     if count <= h:
        #         return k
        # return -1 # If koko can't finish at all, ideally shouldn't reach this ever

        # Binary Search - Time = O(n*log(k)), space = O(1)
        left, right = 1, max(piles)
        while left < right:
            mid = (left + right) // 2
            hrs_spent = 0
            for pile in piles:
                hrs_spent += math.ceil(pile / mid)
            if hrs_spent <= h:
                right = mid
            else:
                left = mid+1
        return right
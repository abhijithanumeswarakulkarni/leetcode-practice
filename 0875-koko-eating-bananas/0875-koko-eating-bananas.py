class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        n = len(piles)
        piles.sort()
        lo, hi = 1, piles[-1]
        mini = -1

        while lo <= hi:
            mid = (lo + hi) // 2
            hLeft = h
            i = 0
            while i < n:
                hLeft -= math.ceil(piles[i] / mid)
                if hLeft < 0:
                    break
                i += 1
            if i == n:
                mini = mid
                hi = mid-1
            else:
                lo = mid + 1
        
        return mini
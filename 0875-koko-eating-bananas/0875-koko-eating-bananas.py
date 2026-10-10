import math

class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        left, right = 1, max(piles)

        while left < right:
            k = (left + right) // 2
            can_eat = True
            h_remaining = h
            for pile in piles:
                h_needed = math.ceil(pile / k)
                h_remaining -= h_needed
                if h_remaining < 0:
                    can_eat = False
                    break
            if can_eat:
                right = k
            else:
                left = k + 1
        
        return left
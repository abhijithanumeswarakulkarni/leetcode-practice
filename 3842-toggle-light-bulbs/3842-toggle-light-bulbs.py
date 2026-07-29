class Solution:
    def toggleLightBulbs(self, bulbs: list[int]) -> list[int]:
        # Freq map - Time = O(n*log(n)), space = O(n)
        from collections import Counter
        freq = Counter(bulbs)
        res = [key for key, value in freq.items() if value % 2 != 0]
        res.sort()
        return res
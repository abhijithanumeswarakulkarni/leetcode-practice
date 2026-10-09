class Solution:
    def mirrorDistance(self, n: int) -> int:
        reverse_n = int(str(n)[::-1])
        return abs(reverse_n - n)
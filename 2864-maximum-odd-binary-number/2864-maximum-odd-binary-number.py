class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        frq = Counter(s)
        m, n = frq['0'], frq['1']
        return '1' * (n-1) + '0' * m + '1'
class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        res = None
        while True:
            digits = [int(x) for x in str(n)]
            prod = 1
            for x in digits:
                prod *= x
            if prod % t == 0:
                res = n
                break
            n += 1
        return res
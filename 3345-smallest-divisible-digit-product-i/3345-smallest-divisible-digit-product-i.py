import math

class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        while True:
            prod = math.prod(map(lambda x: int(x), str(n)))
            if prod % t == 0:
                return n
            n += 1
        
        return -1 # Never reached
class Solution:
    def countValidPrefixes(self, s: str) -> int:
        frq = {'0': 0, '1': 0}
        count = 0

        for char in s:
            frq[char] += 1
            diff = abs(frq['0'] - frq['1'])
            if diff <= 1:
                count += 1
        
        return count
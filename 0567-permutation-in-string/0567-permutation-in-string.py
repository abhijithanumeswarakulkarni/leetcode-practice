from collections import Counter
from copy import deepcopy

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # Brute Force - Time = O(n^2), space = O(n)
        freq = dict(Counter(s1))

        i = 0
        m = len(s1)
        n = len(s2)
        while i < n:
            if s2[i] in freq:
                temp = deepcopy(freq)
                j = i
                while j < n and s2[j] in temp:
                    temp[s2[j]] -= 1
                    if temp[s2[j]] == 0:
                        del temp[s2[j]]
                    j += 1
                print(temp, s2[i])
                if not temp:
                    return True
            i += 1
        
        return False                
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        m, n = len(s), len(t)
        if m > n:
            return False
        
        if m == n:
            return s == t
        
        i, j = 0, 0
        while i < m and j < n:
            if s[i] == t[j]:
                i += 1
            j += 1
        
        return True if i == m else False
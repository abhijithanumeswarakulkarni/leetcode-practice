class Solution:
    def isOneEditDistance(self, s: str, t: str) -> bool:
        if s == t:
            return False
        
        m, n = len(s), len(t)
        
        if abs(m-n) > 1:
            return False
        
        if m == n:
            count  = 0
            for i in range(m):
                if s[i] != t[i]:
                    count += 1
                if count > 1:
                    return False
            return True
        
        if m < n:
            m, n = n, m
            s, t = t, s
        
        count = 0
        i, j = 0, 0
        while i < m and j < n:
            if s[i] != t[j]:
                count += 1
            else:
                j += 1
            i += 1
        return True if count + (m-i) == 1 else False
        
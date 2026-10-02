class Solution:
    def countKeyChanges(self, s: str) -> int:
        n = len(s)
        idx = 1
        res = 0

        while idx < n:
            if s[idx] != s[idx-1] and s[idx] != s[idx-1].upper() and s[idx] != s[idx-1].lower():
                res += 1
            idx += 1
        
        return res
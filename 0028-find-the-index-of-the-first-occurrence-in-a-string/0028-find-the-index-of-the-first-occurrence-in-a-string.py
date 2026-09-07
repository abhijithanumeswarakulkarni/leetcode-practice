class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        m = len(haystack)
        n = len(needle)
        i = 0
        while i < m:
            if haystack[i] == needle[0]:
                j = i
                k = 0
                while j < m and k < n and haystack[j] == needle[k]:
                    j += 1
                    k += 1
                if k == n:
                    return i
            i += 1
        
        return -1
class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        k = len(part)

        while True:
            if part in s:
                i = s.index(part)
                s = s[:i] + s[i+k:]
            else:
                break
        
        return s
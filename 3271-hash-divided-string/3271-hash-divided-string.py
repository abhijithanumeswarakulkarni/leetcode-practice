class Solution:
    def stringHash(self, s: str, k: int) -> str:
        n = len(s)
        res = ""

        for idx in range(0, n, k):
            sub = s[idx: idx + k]
            total = 0
            for char in sub:
                total += ord(char) - ord('a')
            total = total % 26
            res += chr(ord('a') + total)
        
        return res
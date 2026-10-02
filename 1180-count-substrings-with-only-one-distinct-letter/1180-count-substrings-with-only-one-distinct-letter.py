class Solution:
    def countLetters(self, s: str) -> int:
        res = 0
        n = len(s)

        for i in range(n):
            for j in range(i + 1, n + 1):
                if len(set(s[i:j])) == 1:
                    res += 1
                else:
                    break
        return res
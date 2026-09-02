class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        m, n = len(word1), len(word2)
        i, j = 0, 0
        res = ""
        turn = True

        if m <= n:
            while i < m:
                if turn:
                    res += word1[i]
                    i += 1
                else:
                    res += word2[j]
                    j += 1
                turn = not turn
            while j < n:
                res += word2[j]
                j += 1
        else:
            while j < n:
                if turn:
                    res += word1[i]
                    i += 1
                else:
                    res += word2[j]
                    j += 1
                turn = not turn
            while i < m:
                res += word1[i]
                i += 1
        return res
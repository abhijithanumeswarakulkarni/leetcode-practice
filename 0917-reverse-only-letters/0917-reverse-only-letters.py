class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        s = list(s)
        n = len(s)
        i, j = 0, n-1
        while i < j:
            while i < j and not s[i].isalpha():
                i += 1
            while i < j and not s[j].isalpha():
                j -= 1
            s[i], s[j] = s[j], s[i]
            i += 1
            j -= 1

        return "".join(s)
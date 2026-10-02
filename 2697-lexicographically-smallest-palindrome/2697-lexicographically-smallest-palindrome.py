class Solution:
    def makeSmallestPalindrome(self, s: str) -> str:
        n = len(s)
        i, j = 0, n-1
        s = list(s)

        while i < j:
            if s[i] != s[j]:
                s[i] = s[j] = min(s[i], s[j])
            i += 1
            j -= 1
        
        return "".join(s)
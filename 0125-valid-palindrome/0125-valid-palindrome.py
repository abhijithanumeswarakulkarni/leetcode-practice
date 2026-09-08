class Solution:
    def isPalindrome(self, s: str) -> bool:
        forwardS = ""
        reversedS = ""
        n = len(s)
        for i in range(n-1, -1, -1):
            if s[i].isalnum():
                forwardS = s[i].lower() + forwardS
                reversedS += s[i].lower()

        return forwardS == reversedS
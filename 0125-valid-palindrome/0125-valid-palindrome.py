class Solution:
    def isPalindrome(self, s: str) -> bool:
        # # Brute Force - Time = O(n), space = O(n)
        # formatted_s = ''
        # for x in s:
        #     if x.isalnum():
        #         formatted_s += x.lower()
        # return formatted_s == formatted_s[::-1]

        # Two pointer - Time = O(n), space = O(1)
        i = 0
        j = len(s) - 1
        while i < j:
            if not s[i].isalnum():
                i += 1
                continue
            if not s[j].isalnum():
                j -= 1
                continue
            if s[i].lower() != s[j].lower():
                return False
            i += 1
            j -= 1
        return True
            
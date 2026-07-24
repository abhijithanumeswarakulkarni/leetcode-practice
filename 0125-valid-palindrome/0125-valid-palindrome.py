class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Reverse
        formatted_s = ''
        for x in s:
            if x.isalnum():
                formatted_s += x.lower()
        return formatted_s == formatted_s[::-1]
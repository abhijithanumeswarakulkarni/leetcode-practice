class Solution:
    def reverseByType(self, s: str) -> str:
        letters, special = [], []

        for char in s:
            if char.isalpha():
                letters.append(char)
            else:
                special.append(char)
        
        letters = letters[::-1]
        special = special[::-1]
        res = ""
        i, j = 0, 0

        for char in s:
            if char.isalpha():
                res += letters[i]
                i += 1
            else:
                res += special[j]
                j += 1
        
        return res
class Solution:
    def reverseDegree(self, s: str) -> int:
        res = 0
        for index, char in enumerate(s):
            res += (index + 1) * (abs(ord(char) - ord('z')) + 1)
        
        return res
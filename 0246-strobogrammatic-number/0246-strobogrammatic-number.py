class Solution:
    def isStrobogrammatic(self, num: str) -> bool:
        pairs = {
            '6': '9',
            '9': '6',
            '8': '8',
            '1': '1',
            '0': '0'
        }
        res = ""
        for digit in num:
            if digit not in pairs:
                return False
            
            res = pairs[digit] + res
        
        return num == res
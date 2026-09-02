class Solution:
    def reverseWords(self, s: str) -> str:
        res = ""
        n = len(s)
        idx = 0

        while idx < n:
            temp = ""
            while idx < n and s[idx].isalnum():
                temp += s[idx]
                idx += 1
            
            if temp:
                res = " " + temp + res
            
            idx += 1
    
        return res.strip()
class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        m, n = len(str1), len(str2)
        
        # Want str1 to be smallest
        if m > n:
            m, n = n, m
            str1, str2 = str2, str1
        
        for k in range(m, 0, -1):
            pattern = str1[:k]
            if m % k == 0 and n % k == 0 and (pattern * (m // k)) == str1 and (pattern * (n // k)) == str2:
                return pattern
        
        return ""
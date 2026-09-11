class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        n = len(s)
        res = [0] * n

        i = 0
        while i < n:
            if s[i] != c:
                j = i-1
                k = i+1
                while j >= 0 and s[j] != c:
                    j -= 1
                while k < n and s[k] != c:
                    k += 1
                
                if j < 0 and k >= n:
                    continue
                elif j >= 0 and k < n:
                    res[i] = min((i-j), (k-i))
                elif j < 0:
                    res[i] = (k-i)
                else:
                    res[i] = (i-j)
            i += 1
        
        return res
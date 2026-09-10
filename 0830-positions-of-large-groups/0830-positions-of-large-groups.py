class Solution:
    def largeGroupPositions(self, s: str) -> List[List[int]]:
        i, j = 0, 1
        n = len(s)
        res = []
        while i < n:
            while j < n and s[i] == s[j]:
                j += 1
            
            if (j-i) >= 3:
                res.append([i, j-1])

            i = j
            j += 1
        
        return res
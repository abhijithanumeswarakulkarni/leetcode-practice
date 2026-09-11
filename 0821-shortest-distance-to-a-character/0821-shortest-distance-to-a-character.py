class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        # # Brute force
        # n = len(s)
        # res = [0] * n

        # i = 0
        # while i < n:
        #     if s[i] != c:
        #         j = i-1
        #         k = i+1
        #         while j >= 0 and s[j] != c:
        #             j -= 1
        #         while k < n and s[k] != c:
        #             k += 1
                
        #         if j < 0 and k >= n:
        #             continue
        #         elif j >= 0 and k < n:
        #             res[i] = min((i-j), (k-i))
        #         elif j < 0:
        #             res[i] = (k-i)
        #         else:
        #             res[i] = (i-j)
        #     i += 1
        
        # return res

        # One pass - optimal
        cIdxs = []
        for index, letter in enumerate(s):
            if letter == c:
                cIdxs.append(index)
        
        n = len(s)
        k = len(cIdxs)
        res = [0] * n

        i, j = 0, 0
        while i < n:
            if s[i] != c:
                if j == 0:
                    res[i] = abs(cIdxs[j] - i)
                else:
                    res[i] = min(abs(i - cIdxs[j-1]), abs(cIdxs[j] - i))
            else:
                if j < k-1:
                    j += 1
            i += 1
        
        return res
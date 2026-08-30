from collections import Counter

class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:

        # Brute force
        # Edge case
        count = Counter(s)
        if '1' not in s or count['1'] < k:
            return ""

        n = len(s)
        res = s
        for i in range(n):
            for j in range(i+1, n+1):
                sub = s[i:j]
                count = Counter(sub)
                if '1' in count and count['1'] == k and (len(sub) < len(res) or (len(sub) == len(res) and sub < res)):
                    res = sub
        
        return res

        # n = len(s)
        # l, r = 0, 0
        # res = s

        # while r < n:
        #     if k == 0:
        #         res = min(res, s[l:r])
        #         while l < r and k == 0:
        #             if s[l] == '1':
        #                 k += 1
        #             l += 1
        #         continue

        #     if s[r] == '1':
        #         k -= 1
        #     r += 1

        # return res
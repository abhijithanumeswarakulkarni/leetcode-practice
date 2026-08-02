class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        # # Brute force - Time = O(n^2), space = O(1) - TLE
        # res = 0
        # n = len(s)
        # for i in range(n-2):
        #     for j in range(i+3, n+1):
        #         sub_str = s[i:j]
        #         if 'a' in sub_str and 'b' in sub_str and 'c' in sub_str:
        #             res += n-j+1
        #             break
        # return res

        # Sliding window - Time = O(n), space = O(1)
        n = len(s)
        l, r = 0, 0
        res = 0
        freq = {'a': 0, 'b': 0, 'c': 0}
        while r < n:
            if freq['a'] == 0 or freq['b'] == 0 or freq['c'] == 0:
                freq[s[r]] += 1
            
            while freq['a'] > 0 and freq['b'] > 0 and freq['c'] > 0:
                res += (n-r)
                freq[s[l]] -= 1
                l += 1
            r += 1
            
        return res
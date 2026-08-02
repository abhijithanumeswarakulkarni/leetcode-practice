class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l, r = 0, 0
        n = len(s)
        res = 0

        freq = {}
        max_freq = 0
        for i in range(26):
            char = chr(ord('A') + i)
            freq[char] = 0

        while r < n:
            freq[s[r]] += 1
            max_freq = max(max_freq, freq[s[r]])
            while (r-l+1) - max_freq > k:
                freq[s[l]] -= 1
                max_freq = max(freq.values())
                l += 1
            res = max(res, (r-l+1))
            print(l, r, max_freq, res)
            r += 1
        
        return res
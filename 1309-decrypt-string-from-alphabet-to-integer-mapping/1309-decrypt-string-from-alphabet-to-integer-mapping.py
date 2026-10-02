class Solution:
    def freqAlphabets(self, s: str) -> str:
        hmap = {}
        for i in range(26):
            key = str(i + 1)
            value = chr(ord('a') + i)
            if i >= 9:
                key += '#'
            hmap[key] = value
        
        idx = 0
        n = len(s)
        res = ""

        while idx < n:
            if idx + 2 < n and s[idx + 2] == '#':
                res += hmap[s[idx:idx+3]]
                idx += 3
            else:
                res += hmap[s[idx]]
                idx += 1

        return res
class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        n = len(s)
        l, r = 0, 0
        hmap = {}
        k = 2
        maxi = 0

        while r < n:
            if s[r] in hmap:
                hmap[s[r]] += 1
            else:
                hmap[s[r]] = 1
            
            while len(hmap) > k:
                hmap[s[l]] -= 1
                if hmap[s[l]] == 0:
                    del hmap[s[l]]
                l += 1
            maxi = max(maxi, (r-l+1))
            r += 1
        
        return maxi
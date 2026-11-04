class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_len = 0
        l, r = 0, 0
        n = len(s)
        unq = set()

        while r < n:
            while s[r] in unq:
                unq.remove(s[l])
                l += 1
            
            unq.add(s[r])
            max_len = max(max_len, (r - l + 1))
            r += 1
        
        return max_len
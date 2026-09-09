class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        passed = []
        l, r = 0, 0
        n = len(s)
        maxi = 0

        while r < n:
            while l < r and s[r] in passed:
                passed.pop(0)
                l += 1
            
            passed.append(s[r])
            maxi = max(maxi, (r-l+1))
            r += 1
        
        return maxi